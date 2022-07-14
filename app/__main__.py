import falcon
from wsgiref.simple_server import make_server

from .api import userA,connectA,mongoA,mysqlA


app = application = falcon.App()
user =userA.UserR()
heroku=connectA.ConnectR()
mysqldb=mysqlA.MysqlR()
mongodb=mongoA.MongoR()

app.add_route('/user', user)
app.add_route('/heroku', heroku)
app.add_route('/mysql',mysqldb)
app.add_route('/mongo',mongodb)

# waitress-serve --port=8000 app.__main__:app
if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()