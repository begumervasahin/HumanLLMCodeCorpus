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
            'ui_modules': uimodules,
            'ui_methods': uimethods,
            'static_path': b1,
            'cookie_secret': base64.b64encode(uuid.uuid3(uuid.NAMESPACE_DNS, 'android').bytes),
            'sentry_url': 'https:
        }
        super().fonk1(**b3)
        for host, *handlers in b2:
            self.add_handlers(host, handlers)
def fonk2():
    b4 = class1()
    if not options.debug:
        b4.b5 = AsyncSentryClient(b4.b3['sentry_url'])
    b6 = HTTPServer(b4, xheaders=True)
    b6.listen(options.port)
    print(f'Server is running on port {options.port}')
if b7 = = "__main__":
    fonk2()