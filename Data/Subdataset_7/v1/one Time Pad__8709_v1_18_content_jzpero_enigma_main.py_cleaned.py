import os
import sqlite3
import cherrypy
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import base64
b1 = "messages.db"
class class1(object):
    def fonk1(self):
        self.a1 = 32
        self.b2 = Random.new().read(AES.block_size)
    def fonk2(self, s):
        return s + (self.a1 - len(s) % self.a1) * chr(self.a1 - len(s) % self.a1)
    def fonk3(self, s):
        return s[:-ord(s[len(s)-1:])]
    @cherrypy.expose
    @cherrypy.tools.accept(b3 = 'text/plain')
    def fonk4(self, b4 = None, b7=None):
        if b4 and b7:
            return self.fonk5(b4, b7)
        elif b4:
            return self.fonk6(b4)
        else:
            return "Invalid request."
    def fonk5(self, b4, b7):
        b5 = hashlib.sha256(b4.encode()).digest()
        b6 = AES.new(b5, AES.MODE_CBC, self.b2)
        b4 = base64.b64encode(self.b2 + b6.encrypt(self.fonk2(b4)))
        b7 = base64.b64encode(self.b2 + b6.encrypt(self.fonk2(b7)))
        with sqlite3.connect(b1) as c:
            c.execute("INSERT INTO data VALUES (?, ?)", [b4, b7])
        return "Message stored successfully."
    def fonk6(self, b4):
        b5 = hashlib.sha256(b4.encode()).digest()
        b6 = AES.new(b5, AES.MODE_CBC, self.b2)
        b4 = base64.b64encode(self.b2 + b6.encrypt(self.fonk2(b4)))
        with sqlite3.connect(b1) as c:
            b7 = c.execute("SELECT b7 FROM data WHERE b4=?", [b4]).fetchone()
        if b7:
            b7 = base64.b64decode(b7[0])
            return self.fonk3(b6.decrypt(b7[AES.block_size:])).decode('utf-8')
        else:
            return "No b7 found for the given b4."
def fonk7():
    with sqlite3.connect(b1) as con:
        con.execute("CREATE TABLE IF NOT EXISTS data (b4, b7)")
def fonk8():
    with sqlite3.connect(b1) as con:
        con.execute("DROP TABLE IF EXISTS data")
if b8 = = '__main__':
    b9 = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }
    cherrypy.engine.subscribe('start', setup_database)
    cherrypy.engine.subscribe('stop', cleanup_database)
    cherrypy.quickstart(class1(), '/', b9)