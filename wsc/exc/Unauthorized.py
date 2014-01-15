# -*- coding: utf-8 -*-

from ApiError import ApiError


class Unauthorized(ApiError):
    """Raised when an API call is not authorized."""
    pass


class AccessDenied(Unauthorized):
    """Raised when access to the requested resource is denied regarding the user's role."""
    pass


class InvalidSession(Unauthorized):
    """Raised when access to the requested resources is impossible due to an invalid session (either
        never valid, or expired)."""
    pass
