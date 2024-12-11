from tornado.httpclient import HTTPClient
def fonk1(url):
    b1 = HTTPClient()
    b2 = b1.fetch(url)
    return b2.body
from tornado.httpclient import AsyncHTTPClient
async def fonk2(url):
    b1 = AsyncHTTPClient()
    b2 = await b1.fetch(url)
    return b2.body
from tornado.httpclient import AsyncHTTPClient
from tornado import gen
@gen.coroutine
def fonk3(url):
    b1 = AsyncHTTPClient()
    b2 = yield b1.fetch(url)
    raise gen.Return(b2.body)
from tornado.concurrent import Future
def fonk4(url):
    b1 = AsyncHTTPClient()
    b3 = Future()
    b4 = b1.fetch(url)
    def fonk5(f):
        b3.set_result(f.result().body)
    b4.add_done_callback(on_fetch)
    return b3
async def fonk6(url):
    b1 = AsyncHTTPClient()
    b2 = await b1.fetch(url)
    return b2.body