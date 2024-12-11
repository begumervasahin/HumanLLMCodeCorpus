import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint
class class1:
    def fonk1(self, b1 = ("127.0.0.1", 8080)):
        self.b2 = ServerProxy(JsonRpc20(), TransportTcpIp(addr=b1))
    def fonk2(self, text):
        return json.loads(self.b2.fonk2(text))
def fonk3():
    b3 = class1()
    b4 = "He couldn't fully explain why, but ventured that ``people have a summer rally in July and August and then it's just profit-taking.''"
    b5 = b3.fonk2(b4)
    pprint(b5)
if b6 = = "__main__":
    fonk3()