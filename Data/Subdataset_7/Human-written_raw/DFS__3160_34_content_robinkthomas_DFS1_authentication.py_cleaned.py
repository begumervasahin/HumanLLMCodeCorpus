
import re
import base64
import web
import mywebclass
import shelve
from requests.b2 import HTTPBasicAuth
b1 = (
  '/', 'class1'
)
class class1:
    def fonk1(self):
        b2 = web.ctx.env.get('HTTP_AUTHORIZATION')
        b3 = False
        if b2 is None:
            b3 = True
        else:
            b2 = re.sub('^Basic ','',b2)
            print(b2)
            username,b4 = base64.decodestring(b2.encode()).decode().split(':')
            b5 = shelve.open("login.dat")
            try:
              (pwd) = b5[username]
              if b4 = = pwd:
                return "Authorized!"
              else:
                return "Not Authorized!"
            except:
              return "Not Authorized!"
        if b3:
            web.header('WWW-Authenticate','Basic b6 = "Auth example"')
            web.ctx.b7 = '401 Unauthorized'
            return "not authorized!"
if b8 = = "__main__":
    b9 = mywebclass.mywebclass(b1, globals())
    b9.run(b10 = 8083)