import tornado.httpclient
import tornado.gen
import tornado.concurrent
def synchronous_fetch(url):
    with tornado.httpclient.HTTPClient() as http_client:
        response = http_client.fetch(url)
        return response.body
async def asynchronous_fetch(url):
    async with tornado.httpclient.AsyncHTTPClient() as http_client:
        response = await http_client.fetch(url)
        return response.body
@tornado.gen.coroutine
def async_fetch_gen(url):
    http_client = tornado.httpclient.AsyncHTTPClient()
    try:
        response = yield http_client.fetch(url)
        raise tornado.gen.Return(response.body)
    finally:
        http_client.close()
def async_fetch_manual(url):
    http_client = tornado.httpclient.AsyncHTTPClient()
    my_future = tornado.concurrent.Future()
    def on_fetch(future):
        my_future.set_result(future.result().body)
    fetch_future = http_client.fetch(url)
    fetch_future.add_done_callback(on_fetch)
    return my_future
async def fetch_coroutine(url):
    async with tornado.httpclient.AsyncHTTPClient() as http_client:
        response = await http_client.fetch(url)
        return response.body