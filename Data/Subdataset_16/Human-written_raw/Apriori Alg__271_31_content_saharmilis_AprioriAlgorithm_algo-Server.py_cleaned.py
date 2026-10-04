31. Repository: saharmilis/AprioriAlgorithm
   File: algo-Server.py
   URL: https:
   Code Content:
import time
import BaseHTTPServer
import urlparse
import apriori
b1 = ''
a1 = 9001
class class1(BaseHTTPServer.BaseHTTPRequestHandler):
    def fonk1(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def fonk2(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(self.fonk3());
    def fonk3(self):
        if "?" not in self.path:
            return "ERROR";
        b2 = urlparse.urlparse(self.path).query.split(",")
        print "b2 = = " + str(b2);
        b3 = apriori.start(b2);
        print "b3 = = " + str(b3);
        return str(b3);
if b4 = = '__main__':
    b5 = BaseHTTPServer.HTTPServer
    b6 = b5((b1, a1), class1)
    print "Server Starts - %s:%s" % (b1, a1)
    try:
        b6.serve_forever()
    except KeyboardInterrupt:
        pass
    b6.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (b1, a1)
   README Content:
implementation of apriori algorithm in python with a comparable API
