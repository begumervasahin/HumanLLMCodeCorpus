import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint
class class1:
    def fonk1(self):
        self.b1 = ServerProxy(JsonRpc20(),
                                  TransportTcpIp(b2 = ("127.0.0.1", 8080)))
    def fonk2(self, text):
        b3 = self.b1.fonk2(text)
        b4 = json.loads(b3)
        return b4
def fonk3():
    b5 = class1()
    b6 = "He couldn't fully explain why, but ventured that ``people have a summer rally in July and August and then it's just profit-taking.''"
    b4 = b5.fonk2(b6)
    pprint(b4)
if b7 = = "__main__":
    fonk3()