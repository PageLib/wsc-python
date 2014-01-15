# -*- coding: utf-8 -*-


class NotFound(Exception):
    """Raised when a requested resource was not found by the APIs (generally, got a 404)."""
    pass


class TransactionNotFound(NotFound):
    pass


class EntityNotFound(NotFound):
    pass


class UserNotFound(NotFound):
    pass
