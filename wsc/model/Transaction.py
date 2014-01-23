# -*- coding: utf-8 -*-

from Entity import Entity


class Transaction(Entity):
    id = None
    user_id = None
    amount = None
    currency = None
    date_time = None

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'amount': self.amount,
            'currency': self.currency,
            'date_time': self.date_time
        }


class Printing(Transaction):
    copies = None
    pages_grey_levels = None
    pages_color = None

    def to_dict(self):
        d = Transaction.to_dict(self)
        d.update({
            'transaction_type': 'printing',
            'copies': self.copies,
            'pages_grey_levels': self.pages_grey_levels,
            'pages_color': self.pages_color
        })
        return d


class LoadingCreditCard(Transaction):
    def to_dict(self):
        d = Transaction.to_dict(self)
        d.update({
            'transaction_type': 'loading_credit_card'
        })
        return d


class HelpDesk(Transaction):
    def to_dict(self):
        d = Transaction.to_dict(self)
        d.update({
            'transaction_type': 'help_desk'
        })
        return d
