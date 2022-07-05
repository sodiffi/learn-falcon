import falcon
from wsgiref.simple_server import make_server

from .api.user import UserR


app = application = falcon.App()

user = UserR(storage_path='.')
app.add_route('/user', user)
if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()