# -*- coding: utf-8 -*-

from Entity import Entity


class User(Entity):
    id = None
    login = None
    password_hash = None
    first_name = None
    last_name = None
    role = None
    entity_id = None #Faut il passer quand on aura fait les entity à un objet entity (ou faire une
                     # @param entity qui la get.?

    def to_dict(self):
        return {
            'id': self.id,
            'login': self.login,
            'password_hash': self.password_hash,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'role': self.role,
            'entity_id': self.entity_id,
        }
