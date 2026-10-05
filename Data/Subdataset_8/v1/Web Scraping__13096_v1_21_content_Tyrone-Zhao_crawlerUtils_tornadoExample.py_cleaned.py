import tornado.ioloop
from tornado.httpclient import HTTPClient, AsyncHTTPClient
from tornado import gen
from tornado.concurrent import Future
def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body
async def asynchronous_fetch(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return response.body
@gen.coroutine
def async_fetch_gen(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    raise gen.Return(response.body)
def async_fetch_manual(url):
    http_client = AsyncHTTPClient()
    my_future = Future()
    fetch_future = http_client.fetch(url)
    def on_fetch(f):
        my_future.set_result(f.result().body)
    fetch_future.add_done_callback(on_fetch)
    return my_future
async def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return response.body
async def main():
    url = "https:
    sync_result = synchronous_fetch(url)
    print("Synchronous Fetch Result:", sync_result)
    async_result = await asynchronous_fetch(url)
    print("Asynchronous Fetch Result:", async_result)
    async_gen_result = await async_fetch_gen(url)
    print("Asynchronous Fetch with gen.coroutine Result:", async_gen_result)
    async_manual_result = await async_fetch_manual(url)
    print("Asynchronous Fetch with Manual Future Result:", async_manual_result)
    async_coroutine_result = await fetch_coroutine(url)
    print("Asynchronous Fetch using async/await Result:", async_coroutine_result)
if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(main)