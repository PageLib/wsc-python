# -*- coding: utf-8 -*-

import requests
from .Repository import Repository
from wsc.model import LoadingCreditCard, Printing, HelpDesk


class TransactionRepository(Repository):
    """Repository for transactions, uses the invoicing service."""

    def get(self, id):
        url = self.config.invoicing_endpoint + '/v1/transactions/{}'.format(id)
        resp = requests.get(url)
        data = resp.json()

        # Instantiate the appropriate subclass of Transaction based on the 'transaction_type' field
        transaction_type = data['transaction_type']
        if transaction_type == 'loading_credit_card':
            return LoadingCreditCard(**data)
        elif transaction_type == 'printing':
            return Printing(**data)
        elif transaction_type == 'help_desk':
            return HelpDesk(**data)
        else:
            raise ValueError("unknown transaction type '{}'".format(transaction_type))
