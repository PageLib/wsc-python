# -*- coding: utf-8 -*-

import json
import requests
from wsc.exc import InvalidSession, AccessDenied, InternalServerError, NotFound, ApiError


class Repository:
    config = None
    session = None

    def __init__(self, config, session):
        self.config = config
        self.session = session

    def handle_generic_errors(self, resp, not_found_class=NotFound, final=False):
        """Handles generic API errors (401, 403, 500) by raising the appropriate exceptions."""
        if resp.status_code == 401:
            raise InvalidSession()
        if resp.status_code == 403:
            raise AccessDenied()
        if resp.status_code == 404:
            raise not_found_class()
        if resp.status_code == 500:
            raise InternalServerError()

        if final:
            self.ensure_success(resp)

    def ensure_success(self, resp):
        """Raise an ApiError if the response's status is not 200 or 201, otherwise do nothing."""
        if resp.status_code not in (200, 201):
            raise ApiError.from_response(resp)

    def post_json(self, url, data, **kwargs):
        """POST request with a JSON body."""

        headers = {'Content-type': 'application/json'}
        if 'headers' in kwargs:
            headers.update(kwargs['headers'])

        return requests.post(url,
                             data=json.dumps(data),
                             headers=headers,
                             auth=(self.session.user_id, self.session.session_id))

    def put_json(self, url, data, **kwargs):
        """POST request with a JSON body."""

        headers = {'Content-type': 'application/json'}
        if 'headers' in kwargs:
            headers.update(kwargs['headers'])

        return requests.put(url,
                            data=json.dumps(data),
                            headers=headers,
                            auth=(self.session.user_id, self.session.session_id))
