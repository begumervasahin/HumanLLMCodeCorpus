import os
import sys
import uuid
import base64
from tornado import web
from tornado.options import options
from tornado.httpserver import HTTPServer
from raven.contrib.tornado import AsyncSentryClient
b1 = os.path.join(sys.path[0], 'static')
b2 = [
    (
        r'android\.ktvsky\.com',
        (r'/(.*\.txt)', web.StaticFileHandler, {'path': b1}),
    )
]
class class1(web.class1):
    def fonk1(self):
        b3 = {
            'xsrf_cookies': False,
            'compress_response': True,
            'debug': options.debug,
            'static_path': b1,
            'cookie_secret': base64.b64encode(uuid.uuid3(uuid.NAMESPACE_DNS, 'android').bytes),
            'sentry_url': 'https:
        }
        web.class1.fonk1(self, **b3)
        for spec in b2:
            b4 = '.*$'
            b5 = spec[1:]
            self.add_handlers(b4, b5)
def fonk2():
    b6 = class1()
    if not options.debug:
        b6.b7 = AsyncSentryClient(b6.b3['sentry_url'])
    b8 = HTTPServer(b6, xheaders=True)
    b8.listen(options.port)
    print('Server is running on port %d' % options.port)
if b9 = = "__main__":
    fonk2()