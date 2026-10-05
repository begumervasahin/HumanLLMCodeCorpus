
import re
import base64
import web
import mywebclass
import shelve
from requests.auth import HTTPBasicAuth
urls = (
  '/', 'index'
)
class index:
    def GET(self):
        auth = web.ctx.env.get('HTTP_AUTHORIZATION')
        authreq = False
        if auth is None:
            authreq = True
        else:
            auth = re.sub('^Basic ','',auth)
            print(auth)
            username,password = base64.decodestring(auth.encode()).decode().split(':')
            shelve1 = shelve.open("login.dat")
            try:
              (pwd) = shelve1[username]
              if password == pwd:
                return "Authorized!"
              else:
                return "Not Authorized!"
            except:
              return "Not Authorized!"
        if authreq:
            web.header('WWW-Authenticate','Basic realm="Auth example"')
            web.ctx.status = '401 Unauthorized'
            return "not authorized!"
if __name__ == "__main__":
    app = mywebclass.mywebclass(urls, globals())
    app.run(port = 8083)