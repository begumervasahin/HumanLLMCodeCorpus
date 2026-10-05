import tornado.httpclient
import tornado.gen
import tornado.concurrent
def fonk1(url):
    with tornado.httpclient.HTTPClient() as b2:
        b1 = b2.fetch(url)
        return b1.body
async def fonk2(url):
    async with tornado.httpclient.AsyncHTTPClient() as b2:
        b1 = await b2.fetch(url)
        return b1.body
@tornado.gen.coroutine
def fonk3(url):
    b2 = tornado.httpclient.AsyncHTTPClient()
    try:
        b1 = yield b2.fetch(url)
        raise tornado.gen.Return(b1.body)
    finally:
        b2.close()
def fonk4(url):
    b2 = tornado.httpclient.AsyncHTTPClient()
    b3 = tornado.concurrent.Future()
    def fonk5(future):
        b3.set_result(future.result().body)
    b4 = b2.fetch(url)
    b4.add_done_callback(on_fetch)
    return b3
async def fonk6(url):
    async with tornado.httpclient.AsyncHTTPClient() as b2:
        b1 = await b2.fetch(url)
        return b1.body