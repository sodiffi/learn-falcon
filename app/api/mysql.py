import imp
import json
import falcon


from ..database import test

class MysqlR:
    _CHUNK_SIZE_BYTES = 4096

    def on_get(self, req, resp):
        data=test.test()
        doc = {
            'images': [
                {
                    'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
                }
            ]
        }

        resp.text = json.dumps(data, ensure_ascii=False)
        resp.status=falcon.HTTP_200

