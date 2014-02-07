# -*- coding: utf-8 -*-

import requests
from .Repository import Repository
from wsc.model import User
from wsc.exc import UserNotFound


class UserRepository(Repository):
    """Repository for Users, uses the IAM service"""

    def get(self, id):
        """
        Get a user from the IAM service.
        """
        url = self.config.iam_endpoint + '/v1/users/' + id
        resp = requests.get(url,
                            auth=(self.session.user_id, self.session.session_id))
        self.handle_generic_errors(resp, UserNotFound, True)
        return User(**resp.json())

    def create(self, user):
        """
        POST an user in the IAM service.
        """
        d = user.to_dict()
        d.pop('id')
        resp = self.post_json(self.config.iam_endpoint + '/v1/users', d)
        self.handle_generic_errors(resp, final=True)

        # TODO: gestion des différents cas de 412
        return User(**(resp.json()))

    def delete(self, user):
        id = user.id
        resp = requests.delete(self.config.iam_endpoint + '/v1/users/' + id)
        self.handle_generic_errors(resp, final=True)

        # TODO: gestion des différents cas de 412

    def put(self, user):
        id = user.id
        d = user.to_dict()
        resp = self.put_json(self.config.iam_endpoint + '/v1/users', d)
        self.handle_generic_errors(resp, final=True)

        # TODO: gestion des différents cas de 412
        return User(**(resp.json()))
