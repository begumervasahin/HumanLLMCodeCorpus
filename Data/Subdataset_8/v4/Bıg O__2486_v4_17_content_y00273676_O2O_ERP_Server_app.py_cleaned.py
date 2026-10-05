import os
import sys
import uuid
import base64
from tornado import web
from tornado.options import options
from tornado.httpserver import HTTPServer
from raven.contrib.tornado import AsyncSentryClient
STATIC_PATH = os.path.join(sys.path[0], 'static')
URLS = [
    (r'android\.ktvsky\.com',
        (r'/(.*\.txt)', web.StaticFileHandler, {'path': STATIC_PATH}),
    )
]
class Application(web.Application):
    def __init__(self):
        settings = {
            'xsrf_cookies': False,
            'compress_response': True,
            'debug': options.debug,
            'ui_modules': uimodules,
            'ui_methods': uimethods,
            'static_path': STATIC_PATH,
            'cookie_secret': base64.b64encode(uuid.uuid3(uuid.NAMESPACE_DNS, 'android').bytes),
            'sentry_url': 'https:
        }
        web.Application.__init__(self, **settings)
        for spec in URLS:
            host = '.*$'
            handlers = spec[1:]
            self.add_handlers(host, handlers)
def run():
    app = Application()
    if not options.debug:
        app.sentry_client = AsyncSentryClient(app.settings['sentry_url'])
    http_server = HTTPServer(app, xheaders=True)
    http_server.listen(options.port)
    print('Server is running on port %d' % options.port)
if __name__ == "__main__":
    run()