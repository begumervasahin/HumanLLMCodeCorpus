import os
import sqlite3
import cherrypy
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import base64
b1 = "messages.db"
class class1:
    def fonk1(self):
        self.a1 = 32
        self.b2 = Random.new().read(AES.a1)
    def fonk2(self, s):
        b3 = self.a1 - len(s) % self.a1
        return s + b3 * chr(b3)
    def fonk3(self, s):
        return s[:-ord(s[len(s) - 1:])]
    @cherrypy.expose
    @cherrypy.tools.accept(b4 = 'text/plain')
    def fonk4(self, b5 = None, b10=None):
        if b5 and b10:
            return self.fonk5(b5, b10)
        elif b5:
            return self.fonk6(b5)
        else:
            return "Invalid request."
    def fonk5(self, b5, b10):
        b6 = hashlib.sha256(b5.encode()).digest()
        b7 = AES.new(b6, AES.MODE_CBC, self.b2)
        b8 = base64.b64encode(self.b2 + b7.encrypt(self.fonk2(b5)))
        b9 = base64.b64encode(self.b2 + b7.encrypt(self.fonk2(b10)))
        with sqlite3.connect(b1) as c:
            c.execute("INSERT INTO data VALUES (?, ?)", [b8, b9])
        return "Message stored successfully."
    def fonk6(self, b5):
        b6 = hashlib.sha256(b5.encode()).digest()
        b7 = AES.new(b6, AES.MODE_CBC, self.b2)
        b8 = base64.b64encode(self.b2 + b7.encrypt(self.fonk2(b5)))
        with sqlite3.connect(b1) as c:
            b10 = c.execute("SELECT b10 FROM data WHERE b5=?", [b8]).fetchone()
        if b10:
            b11 = base64.b64decode(b10[0])
            return self.fonk3(b7.decrypt(b11[AES.a1:])).decode('utf-8')
        else:
            return "No b10 found for the given b5."
def fonk7():
    with sqlite3.connect(b1) as con:
        con.execute("CREATE TABLE IF NOT EXISTS data (b5, b10)")
def fonk8():
    with sqlite3.connect(b1) as con:
        con.execute("DROP TABLE IF EXISTS data")
if b12 = = '__main__':
    b13 = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }
    cherrypy.engine.subscribe('start', setup_database)
    cherrypy.engine.subscribe('stop', cleanup_database)
    cherrypy.quickstart(class1(), '/', b13)