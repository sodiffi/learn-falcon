
import imp
import json
import falcon
from app.api import checkParm, default
from ..database import translate



class TranslateR:

    _CHUNK_SIZE_BYTES = 4096



    # This is the method we implemented before
    def on_get(self, req, resp):
        doc = {
            'images': [
                {
                    'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
                }
            ]
        }

        resp.data = json.dumpS(doc)
        resp.content_type = falcon.MEDIA_MSGPACK
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        raw_json = req.bounded_stream.read()
        cond=["video_id","user_id","start_time","end_time","text"]
        data=json.loads(raw_json)
        t=checkParm(cond,data)
        print(data["video_id"])
        print(t)
        if(t == ""):
            res = translate.create(data)
        else:
            res = {"success": False, "mes": t}
        resp.text=res
        resp.status = falcon.HTTP_201
      