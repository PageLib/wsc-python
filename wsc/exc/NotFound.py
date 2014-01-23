# -*- coding: utf-8 -*-

from ApiError import ApiError


class NotFound(ApiError):
    """Raised when a requested resource was not found by the APIs (generally, got a 404)."""
    pass


class TransactionNotFound(NotFound):
    pass


class EntityNotFound(NotFound):
    pass


class UserNotFound(NotFound):
    pass


class AclResourceNotFound(NotFound):
    """Raised by IAM when checking a permission for a non-existing resource (not declared in
        iam/roles.py)."""

    resource_name = None

    def __init__(self, resource_name):
        self.resource_name = resource_name

    def __str__(self):
        return self.resource_name

    def __unicode__(self):
        return unicode(__str__(self))
