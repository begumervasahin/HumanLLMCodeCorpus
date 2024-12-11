import tornado.httpclient
import tornado.gen
import tornado.concurrent
def fonk1(url):
    b1 = tornado.httpclient.HTTPClient()
    b2 = b1.fetch(url)
    return b2.body
async def fonk2(url):
    b1 = tornado.httpclient.AsyncHTTPClient()
    b2 = await b1.fetch(url)
    return b2.body
@tornado.gen.coroutine
def fonk3(url):
    b1 = tornado.httpclient.AsyncHTTPClient()
    b2 = yield b1.fetch(url)
    raise tornado.gen.Return(b2.body)
def fonk4(url):
    b1 = tornado.httpclient.AsyncHTTPClient()
    b3 = tornado.concurrent.Future()
    def fonk5(future):
        b3.set_result(future.result().body)
    b4 = b1.fetch(url)
    b4.add_done_callback(on_fetch)
    return b3
async def fonk6(url):
    b1 = tornado.httpclient.AsyncHTTPClient()
    b2 = await b1.fetch(url)
    return b2.body