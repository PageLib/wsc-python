# -*- coding: utf-8 -*-

from ApiError import ApiError


class Unauthorized(ApiError):
    """Raised when an API call is not authorized."""
    pass


class AccessDenied(Unauthorized):
    """Raised when access to the requested resource is denied regarding the user's role."""
    action = None
    resource = None

    def __init__(self, action, resource):
        self.action = action
        self.resource = resource

        super(Exception, self).__init__('{} {}: access denied'.format(action, resource))


class InvalidSession(Unauthorized):
    """Raised when access to the requested resources is impossible due to an invalid session (either
        never valid, or expired)."""
    pass


class InvalidCredentials(ApiError):
    """Raised when a session could not be opened because of invalid credentials."""
    pass
