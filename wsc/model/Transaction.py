# -*- coding: utf-8 -*-


class Transaction:
    id = None
    user_id = None
    amount = None
    currency = None
    date_time = None


class Printing(Transaction):
    copies = None
    pages_grey_levels = None
    pages_color = None


class LoadingCreditCard(Transaction):
    pass


class HelpDesk(Transaction):
    pass
