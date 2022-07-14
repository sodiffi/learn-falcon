import falcon
from wsgiref.simple_server import make_server

from .api import userA,connectA,translateA


app = application = falcon.App()
user =userA.UserR()
heroku=connectA.ConnectR()
translate=translateA.TranslateR()

app.add_route('/user', user)
app.add_route('/heroku', heroku)
app.add_route('/translate',translate)

# waitress-serve --port=8000 app.__main__:app
if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()