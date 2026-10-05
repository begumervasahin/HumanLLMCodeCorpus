import requests
import cgi
import errno
import os
import urlparse
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from requests_toolbelt import MultipartEncoder
CONNECTION_ABORTED = "Connection aborted. Please try again later."
REQUEST_FAILED = "Request failed. Please try again later."
CONNECTION_ECONNRESET = ("The remote system could not complete the request. "
                         "Please try again later."
                        )
JSON_DECODING_FAILURE = ("The remote system has encountered a technical problem. "
                         "Please try again later."
                         )
class WebAPIException(Exception):
    def __init__(self, msg, *args, **kwargs):
        super(WebAPIException, self).__init__(msg, *args, **kwargs)
        if isinstance(msg, dict):
            self.dict = msg
        else:
            self.dict = {'error': msg}
    def __str__(self):
        return str(self.dict)
class WebAPI(object):
    CHUNK_SIZE = 1024
    def __init__(self, headers, cookies=None):
        self.session = requests.session()
        if headers:
            self.session.headers.update(headers)
        self.cookies = cookies
    @classmethod
    def is_success(cls, code):
        return 200 <= code <= 299
    def update_cookies(self):
        cookies = self.session.cookies.get_dict()
        if cookies:
            if self.cookies:
                self.cookies.update(cookies)
            else:
                self.cookies = cookies
    def get(self, url, stream=None, **kwargs):
        try:
            kwargs.pop('cookies', None)
            response = self.session.get(url, cookies=self.cookies, stream=stream, **kwargs)
        except requests.ConnectionError:
            raise WebAPIException(CONNECTION_ABORTED)
        except OSError as e:
            if e.errno == errno.ECONNRESET:
                raise WebAPIException(CONNECTION_ECONNRESET)
            raise
        if not self.is_success(response.status_code):
            raise WebAPIException(REQUEST_FAILED)
        self.update_cookies()
        return response
    def get_file(self, url, stream=True, **kwargs):
        response = self.get(url, stream=stream, **kwargs)
        try:
            params = cgi.parse_header(response.headers['content-disposition'])[1]
            filename = params["filename"]
        except (KeyError, IndexError):
            path = urlparse.urlparse(response.url).path
            filename = os.path.basename(path).strip() or None
            if filename and not isinstance(filename, str):
                filename = str(filename, 'utf-8')
        if stream:
            return filename, response.iter_content(self.CHUNK_SIZE)
        return filename, response.content
    def post(self, url, data, **kwargs):
        try:
            response = self.session.post(url, data, cookies=self.cookies, **kwargs)
        except requests.ConnectionError:
            raise WebAPIException(CONNECTION_ABORTED)
        except OSError as e:
            if e.errno == errno.ECONNRESET:
                raise WebAPIException(CONNECTION_ECONNRESET)
            raise
        if not self.is_success(response.status_code):
            raise WebAPIException(REQUEST_FAILED)
        self.update_cookies()
        return response
    def put(self, url, data=None, **kwargs):
        try:
            kwargs.pop('cookies', None)
            response = self.session.put(url, data=data, cookies=self.cookies, **kwargs)
        except requests.ConnectionError:
            raise WebAPIException(CONNECTION_ABORTED)
        except OSError as e:
            if e.errno == errno.ECONNRESET:
                raise WebAPIException(CONNECTION_ECONNRESET)
            raise
        if not self.is_success(response.status_code):
            raise WebAPIException(REQUEST_FAILED)
        self.update_cookies()
        return response
    def validate(self):
        pass
    def parse(self, beautiful_html):
        return beautiful_html
    def beautifulsoup(self, html):
        return BeautifulSoup(html, features="html.parser")
    def webpost(self, url, data, **kwargs):
        self.validate()
        response = self.post(url, data, **kwargs)
        return self.parse(self.beautifulsoup(response.content))
    def webget(self, url, **kwargs):
        return self.beautifulsoup(self.get(url, **kwargs).content)
    def ajaxget(self, url, **kwargs):
        response = self.get(url=url,
                            headers={'X-Requested-With': 'XMLHttpRequest'},
                            **kwargs
                           )
        try:
            return response.json()
        except ValueError:
            raise WebAPIException(JSON_DECODING_FAILURE)
    def ajaxpost(self, url, data=None, **kwargs):
        self.validate()
        response = self.post(url=url, data=data or {},
                             headers={'X-Requested-With': 'XMLHttpRequest'},
                             **kwargs
                            )
        content_type = cgi.parse_header(response.headers['Content-Type'])[0]
        if 'html' in content_type:
            return self.parse(self.beautifulsoup(response.content))
        if 'json' in content_type:
            try:
                return response.json()
            except ValueError:
                raise WebAPIException(JSON_DECODING_FAILURE)
        return response
    def ajaxput(self, url, data=None, **kwargs):
        self.validate()
        response = self.put(url=url, data=data or {},
                            headers={'X-Requested-With': 'XMLHttpRequest'},
                            **kwargs
                           )
        content_type = cgi.parse_header(response.headers['Content-Type'])[0]
        if 'html' in content_type:
            return self.parse(self.beautifulsoup(response.content))
        if 'json' in content_type:
            try:
                return response.json()
            except ValueError:
                raise WebAPIException(JSON_DECODING_FAILURE)
        return response
    def multipart_upload(self, url, data=None, **kwargs):
        self.validate()
        encoder = MultipartEncoder(fields=data)
        response = self.post(url=url, data=encoder,
                             headers={'Content-Type': encoder.content_type,
                                      'Content-Length': str(encoder.len),
                                     },
                             **kwargs
                            )
        return self.parse(self.beautifulsoup(response.content))
    def show_captcha(self, url):
        _, content_iterator = self.get_file(url)
        imagebytes = b''.join(content_iterator)
        in_memory_file = BytesIO(imagebytes)
        Image.open(in_memory_file).show()
if __name__ == "__main__":
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}