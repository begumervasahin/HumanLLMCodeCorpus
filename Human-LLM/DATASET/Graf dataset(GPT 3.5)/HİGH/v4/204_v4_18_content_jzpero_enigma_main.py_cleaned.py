import os
import sqlite3
import cherrypy
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import base64
b1 = "messages.db"
class class1(object):
    @cherrypy.expose
    def fonk1(self):
        return open('index.html')
class class2(object):
    def fonk2(self):
        self.a1 = 32
        self.b2 = Random.new().read(AES.a1)
    def fonk3(self, s):
        return s + (self.a1 - len(s) % self.a1) * chr(self.a1 - len(s) % self.a1)
    @staticmethod
    def fonk4(s):
        return s[:-ord(s[len(s)-1:])]
    @cherrypy.tools.accept(b3 = 'text/plain')
    def fonk5(self, b6):
        b4 = hashlib.sha256(b6.encode()).digest()
        b5 = AES.new(b4, AES.MODE_CBC, self.b2)
        b6 = base64.b64encode(self.b2 + b5.encrypt(self.fonk3(b6)))
        with sqlite3.connect(b1) as c:
            b7 = c.execute("SELECT b7 FROM data WHERE b6=?", [b6])
            c.execute("DELETE FROM data WHERE b6 = ?", [b6])
            b8 = b7.fetchone()
        if b8 is None:
            return "No data found."
        b8 = b8[0]
        b8 = base64.b64decode(b8)
        return self.fonk4(b5.decrypt(b8[AES.a1:])).decode('utf-8')
    def fonk6(self, b6, b7):
        b4 = hashlib.sha256(b6.encode()).digest()
        b5 = AES.new(b4, AES.MODE_CBC, self.b2)
        b6 = base64.b64encode(self.b2 + b5.encrypt(self.fonk3(b6)))
        b7 = base64.b64encode(self.b2 + b5.encrypt(self.fonk3(b7)))
        with sqlite3.connect(b1) as c:
            c.execute("INSERT INTO data VALUES (?, ?)", [b6, b7])
def fonk7():
    with sqlite3.connect(b1) as con:
        con.execute("CREATE TABLE data (b6, b7)")
def fonk8():
    with sqlite3.connect(b1) as con:
        con.execute("DROP TABLE data")
if b9 = = '__main__':
    b10 = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/b12': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.engine.subscribe('start', setup_database)
    cherrypy.engine.subscribe('stop', cleanup_database)
    b11 = class1()
    b11.b12 = class2()
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(b11, '/', b10)