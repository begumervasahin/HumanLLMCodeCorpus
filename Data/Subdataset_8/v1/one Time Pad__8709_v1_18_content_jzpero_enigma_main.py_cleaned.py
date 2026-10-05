import os
import sqlite3
import cherrypy
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import base64
DB_STRING = "messages.db"
class MessageStorage(object):
    def __init__(self):
        self.bs = 32
        self.iv = Random.new().read(AES.block_size)
    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)
    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]
    @cherrypy.expose
    @cherrypy.tools.accept(media='text/plain')
    def index(self, code=None, message=None):
        if code and message:
            return self.store_message(code, message)
        elif code:
            return self.retrieve_message(code)
        else:
            return "Invalid request."
    def store_message(self, code, message):
        key = hashlib.sha256(code.encode()).digest()
        cipher = AES.new(key, AES.MODE_CBC, self.iv)
        code = base64.b64encode(self.iv + cipher.encrypt(self._pad(code)))
        message = base64.b64encode(self.iv + cipher.encrypt(self._pad(message)))
        with sqlite3.connect(DB_STRING) as c:
            c.execute("INSERT INTO data VALUES (?, ?)", [code, message])
        return "Message stored successfully."
    def retrieve_message(self, code):
        key = hashlib.sha256(code.encode()).digest()
        cipher = AES.new(key, AES.MODE_CBC, self.iv)
        code = base64.b64encode(self.iv + cipher.encrypt(self._pad(code)))
        with sqlite3.connect(DB_STRING) as c:
            message = c.execute("SELECT message FROM data WHERE code=?", [code]).fetchone()
        if message:
            message = base64.b64decode(message[0])
            return self._unpad(cipher.decrypt(message[AES.block_size:])).decode('utf-8')
        else:
            return "No message found for the given code."
def setup_database():
    with sqlite3.connect(DB_STRING) as con:
        con.execute("CREATE TABLE IF NOT EXISTS data (code, message)")
def cleanup_database():
    with sqlite3.connect(DB_STRING) as con:
        con.execute("DROP TABLE IF EXISTS data")
if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }
    cherrypy.engine.subscribe('start', setup_database)
    cherrypy.engine.subscribe('stop', cleanup_database)
    cherrypy.quickstart(MessageStorage(), '/', conf)