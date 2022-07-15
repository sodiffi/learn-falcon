import imp
import json
import falcon
from ..database import db, fordb


class ConnectR:
    _CHUNK_SIZE_BYTES = 4096

    def on_get(self, req, resp):
        data=db.test()
        doc = {
            'images': [
                {
                    'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
                }
            ]
        }

        resp.text = data
        resp.status=falcon.HTTP_200
