import json
from jsonrpc import ServerProxy, JsonRpc20, TransportTcpIp
from pprint import pprint
class StanfordNLP:
    def __init__(self):
        self.server = ServerProxy(JsonRpc20(),
                                  TransportTcpIp(addr=("127.0.0.1", 8080)))
    def parse(self, text):
        response = self.server.parse(text)
        parsed_result = json.loads(response)
        return parsed_result
def main():
    nlp = StanfordNLP()
    text_to_parse = "He couldn't fully explain why, but ventured that ``people have a summer rally in July and August and then it's just profit-taking.''"
    parsed_result = nlp.parse(text_to_parse)
    pprint(parsed_result)
if __name__ == "__main__":
    main()