import json

class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, list):
            
