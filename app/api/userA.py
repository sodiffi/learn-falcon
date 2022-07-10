import json
import falcon


class UserR:

    _CHUNK_SIZE_BYTES = 4096
    # This is the method we implemented before
    def on_get(self, req, resp):
        doc = {
            'hello world': [
                "./heroku",
                "./mongo",
                "./mysql"
            ]
        }

        resp.text = json.dumps(doc, ensure_ascii=False)
        resp.status=falcon.HTTP_200        

    