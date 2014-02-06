# -*- coding: utf-8 -*-


class ApiError(Exception):
    """Base class for all API errors."""

    status_code = None
    data = None

    def __init__(self, status_code=None, data=None):
        self.status_code = status_code
        self.data = data

    @classmethod
    def from_response(cls, resp):
        """Build an instance from a (supposedly failed) Requests response."""
        try:
            data = resp.json()
        except ValueError:
            data = None

        return cls(resp.status_code, data)
