# -*- coding: utf-8 -*-

import requests
from .Repository import Repository


class DocumentRepository(Repository):

    def upload(self, name, local_path):
        # Post metadata and retrieve the document ID
        url_meta = self.config.docs_endpoint + '/v1/docs'
        resp_meta = self.post_json(url_meta, {
            'user_id': self.session.user_id,
            'name': name
        })
        doc_id = resp_meta.json()['id']

        # Post the raw content
        url_raw = self.config.docs_endpoint + '/v1/docs/{}/raw'.format(doc_id)
        requests.post(url_raw,
                      files={'doc': ('doc', open(local_path, 'r'))},
                      auth=(self.session.user_id, self.session.session_id))
