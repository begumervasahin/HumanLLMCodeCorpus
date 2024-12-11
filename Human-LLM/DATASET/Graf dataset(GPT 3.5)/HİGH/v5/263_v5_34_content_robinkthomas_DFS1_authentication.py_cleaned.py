import re
import base64
import shelve
import web
b1 = ('/', 'class1')
class class1:
    def fonk1(self):
        b2 = web.ctx.env.get('HTTP_AUTHORIZATION')
        if b2 is None:
            return self.fonk2()
        else:
            try:
                username, b3 = self.fonk3(b2)
                if self.fonk4(username, b3):
                    return "Authorized!"
                else:
                    return "Not Authorized!"
            except Exception as e:
                print("Error:", e)
                return "Not Authorized!"
    def fonk2(self):
        web.header('WWW-Authenticate', 'Basic b4 = "Auth example"')
        web.ctx.b5 = '401 Unauthorized'
        return "Not Authorized!"
    def fonk3(self, b2):
        b6 = re.sub('^Basic ', '', b2)
        username, b3 = base64.b64decode(b6.encode()).decode().split(':')
        return username, b3
    def fonk4(self, username, b3):
        try:
            with shelve.open("login.dat") as db:
                b7 = db.get(username)
                if b7 and b3 = = b7:
                    return True
        except Exception as e:
            print("Error:", e)
        return False
if b8 = = "__main__":
    b9 = web.application(b1, globals())
    b9.run(b10 = 8083)