import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint
class StanfordNLP:
    def __init__(self, server_address=("127.0.0.1", 8080)):
        self.server = ServerProxy(JsonRpc20(), TransportTcpIp(addr=server_address))
    def parse(self, text):
        return json.loads(self.server.parse(text))
def main():
    nlp = StanfordNLP()
    sample_text = "He couldn't fully explain why, but ventured that ``people have a summer rally in July and August and then it's just profit-taking.''"
    parsed_result = nlp.parse(sample_text)
    pprint(parsed_result)
if __name__ == "__main__":
    main()