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
        resp = requests.get(url)
        self.handle_generic_errors(resp, UserNotFound, True)
        return User(resp.json())

    def create(self, user):
        d = user.to_dict()
        d.pop('id')
        resp = self.post_json(self.config.iam_endpoint + '/v1/users/', d)
        self.handle_generic_errors(resp, final=True)

        # TODO: gestion des différents cas de 412
        return User(resp.json())
