import tornado.ioloop
from tornado.httpclient import HTTPClient, AsyncHTTPClient
from tornado import gen
from tornado.concurrent import Future
def fonk1(b5):
    with HTTPClient() as b2:
        b1 = b2.fetch(b5)
        return b1.body
async def fonk2(b5):
    async with AsyncHTTPClient() as b2:
        b1 = await b2.fetch(b5)
        return b1.body
@gen.coroutine
def fonk3(b5):
    b2 = AsyncHTTPClient()
    b1 = yield b2.fetch(b5)
    raise gen.Return(b1.body)
def fonk4(b5):
    b2 = AsyncHTTPClient()
    b3 = Future()
    def fonk5(future_response):
        b3.set_result(future_response.result().body)
    b4 = b2.fetch(b5)
    b4.add_done_callback(on_fetch)
    return b3
async def fonk6(b5):
    async with AsyncHTTPClient() as b2:
        b1 = await b2.fetch(b5)
        return b1.body
async def fonk7():
    b5 = "https:
    b6 = fonk1(b5)
    print("Synchronous Fetch Result:", b6)
    b7 = await fonk2(b5)
    print("Asynchronous Fetch Result:", b7)
    b8 = await fonk3(b5)
    print("Asynchronous Fetch with gen.coroutine Result:", b8)
    b9 = await fonk4(b5)
    print("Asynchronous Fetch with Manual Future Result:", b9)
    b10 = await fonk6(b5)
    print("Asynchronous Fetch using async/await Result:", b10)
if b11 = = "__main__":
    tornado.ioloop.IOLoop.current().run_sync(main)