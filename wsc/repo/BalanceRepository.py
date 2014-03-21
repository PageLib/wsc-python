# -*- coding: utf-8 -*-

import requests
from .Repository import Repository


class BalanceRepository(Repository):
    """Repository to get a user's balance."""

    def get(self, user_id):
        url = self.config.invoicing_endpoint + '/v1/user/{}/balance'.format(user_id)
        resp = self.auth_get(url)
        self.handle_generic_errors(resp, final=True)
        return float(resp.json()['balance'])
