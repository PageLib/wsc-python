# -*- coding: utf-8 -*-


class ApiError(Exception):
    """Base class for all API errors."""

    status_code = None
    data = None

    def __init__(self, status_code, data):
        self.status_code = status_code
        self.data = data

    @staticmethod
    def from_response(resp):
        """Build an ApiError from a (supposedly failed) Requests response."""
        try:
            data = resp.json()
        except ValueError:
            data = None

        return ApiError(resp.status_code, data)
