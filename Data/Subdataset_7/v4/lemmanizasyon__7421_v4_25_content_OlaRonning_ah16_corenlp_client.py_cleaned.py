import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint
class class1:
    def fonk1(self):
        self.b1 = ServerProxy(JsonRpc20(), TransportTcpIp(addr=("127.0.0.1", 8080)))
    def fonk2(self, text):
        return json.loads(self.b1.fonk2(text))
b2 = class1()
b3 = b2.fonk2("He couldn't fully explain why, but ventured that ``people have a summer rally in July and August and then it's just profit-taking.''")
pprint(b3)