# -*- coding: utf-8 -*-

"""IAM API access and sessions management."""

import requests
import json
from exc import NotFound, InternalServerError, InvalidCredentials, AccessDenied, InvalidSession, AclResourceNotFound,Unauthorized


class Session:
    user_id = None
    session_id = None

    def __init__(self, user_id, session_id):
        self.user_id = user_id
        self.session_id = session_id


class IAM:
    config = None

    def __init__(self, config):
        self.config = config

    def login(self, user_login, password_hash):
        """Logs the user in, returning a Session on success or raising an exception otherwise."""
        url = self.config.iam_endpoint + '/v1/login'
        data = {
            'login': user_login,
            'password_hash': password_hash
        }
        resp = requests.post(url, json.dumps(data), headers={'Content-type': 'application/json'})

        if resp.status_code == 404:
            raise NotFound.from_response(resp)
        if resp.status_code == 412:
            raise InvalidCredentials.from_response(resp)
        if resp.status_code != 200:
            raise InternalServerError.from_response(resp)

        resp_data = resp.json()
        return Session(resp_data['user_id'], resp_data['session_id'])

    def logout(self, session):
        """Logs the user out and returns None."""
        url = self.config.iam_endpoint + '/v1/sessions/{}/logout'.format(session.session_id)
        resp = requests.post(url)

        if resp.status_code == 404:
            raise NotFound.from_response(resp)
        if resp.status_code != 200:
            raise InternalServerError.from_response(resp)

    def is_allowed(self, session, action, resource):
        """Checks whether the user is allowed to perform an action over a resource, returns True if
            so, else returns False."""
        url = self.config.iam_endpoint + '/v1/sessions/{}/{}/permission/{}/{}'.format(
            session.user_id, session.session_id, action, resource)
        resp = requests.get(url)

        if resp.status_code == 404:
            error_code = resp.json()['error']
            if error_code == 'invalid_session':
                raise InvalidSession()
            if error_code == 'invalid_resource':
                raise AclResourceNotFound()
            if error_code == 'session_expired':
                raise AccessDenied(action, resource)

        if resp.status_code != 200:
            raise InternalServerError.from_response(resp)

        return bool(resp.json()['allowed'])

    def ensure_allowed(self, session, action, resource):
        """Ensures a user is allowed to perform an action over a resource."""
        if not self.is_allowed(session, action, resource):
            raise AccessDenied(action, resource)
