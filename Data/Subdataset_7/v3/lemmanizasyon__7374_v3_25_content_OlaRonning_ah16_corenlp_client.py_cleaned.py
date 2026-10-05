import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint
class class1:
    def fonk1(self):
        self.b1 = ServerProxy(
            b2 = JsonRpc20(),
            b3 = TransportTcpIp(addr=("127.0.0.1", 8080))
        )
    def fonk2(self, text):
        b4 = self.b1.fonk2(text)
        b5 = json.loads(b4)
        return b5
def fonk3():
    b6 = class1()
    b7 = "He couldn't fully explain why, but ventured that ``people have a summer rally in July and August and then it's just profit-taking.''"
    b5 = b6.fonk2(b7)
    pprint(b5)
if b8 = = "__main__":
    fonk3()