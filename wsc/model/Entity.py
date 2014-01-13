# -*- coding: utf-8 -*-


class Entity:

    def __init__(self, **kwargs):
        """Automatic initialization of attributes when provided in keyword args."""
        for (k, v) in kwargs.iteritems():
            if hasattr(self, k):
                setattr(self, k, v)
