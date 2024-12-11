import re
import base64
import shelve
import web
from requests.auth import HTTPBasicAuth
b1 = ('/', 'class1')
class class1:
    def fonk1(self):
        b2 = web.ctx.env.get('HTTP_AUTHORIZATION')
        if b2 is None:
            self.fonk2()
        else:
            b3 = re.sub('^Basic ', '', b2)
            try:
                username, b4 = base64.b64decode(b3.encode()).decode().split(':')
                if self.fonk3(username, b4):
                    return "Authorized!"
                else:
                    return "Not Authorized!"
            except Exception as e:
                print("Error:", e)
                return "Not Authorized!"
    def fonk2(self):
        web.header('WWW-Authenticate', 'Basic b5 = "Auth example"')
        web.ctx.b6 = '401 Unauthorized'
        return "Not Authorized!"
    def fonk3(self, username, b4):
        try:
            with shelve.open("login.dat") as db:
                b7 = db.get(username)
                if b7 and b4 = = b7:
                    return True
        except Exception as e:
            print("Error:", e)
        return False
if b8 = = "__main__":
    b9 = web.application(b1, globals())
    b9.run(b10 = 8083)