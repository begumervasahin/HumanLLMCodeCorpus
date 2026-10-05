
from socket import error as SocketError
import requests, cgi, errno, os, urlparse
from BeautifulSoup import BeautifulSoup
from PIL import Image
from StringIO import StringIO
from requests_toolbelt import MultipartEncoder
CONNECTION_ABORTED = "Connection aborted. Try again later."
REQUEST_FAILED = "Request failed. Try again later."
INVALID_REQUEST = "Invalid request. Try again."
CONNECTION_ECONNRESET = ("Remote system could not complete request. "
                         "Please try after some time."
                        )
JASON_DECODING_FAILURE = ("Remote system has encountered some technical problem. "
                          "Please try after some time."
                          )
class WebAPIException(Exception):
    def __init__(self, msg, *args, **kwargs):
        super(WebAPIException, self).__init__(msg, *args, **kwargs)
        if isinstance(msg, dict):
            self.dict = msg
        else:
            self.dict = { 'error': msg }
    def __str__(self):
        return str(self.dict)
class WebAPI(object):
    ITER_CHUNK_SIZE = 1024
    def __init__(self, headers, cookies=None):
        self.session = requests.session()
        if headers:
            self.session.headers.update(headers)
        self.cookies = cookies
    @classmethod
    def is_success(cls, code):
        return code >= 200 and code <= 299
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
        except requests.ConnectionError as e:
            raise WebAPIException(CONNECTION_ABORTED)
        except SocketError as e:
            if e.errno == errno.ECONNRESET:
                raise WebAPIException(CONNECTION_ECONNRESET)
            raise e
        if not self.is_success(response.status_code):
            raise WebAPIException(REQUEST_FAILED)
        self.update_cookies()
        return response
    def get_file(self, url, stream=True, **kwargs):
        response = self.get(url, stream=stream, **kwargs)
        try:
            params = cgi.parse_header(response.headers['content-disposition'])[1]
            filename = params["filename"]
        except (KeyError, IndexError) as e:
            path = urlparse.urlparse(response.url).path
            filename = os.path.basename(path).strip() or None
            if filename and not isinstance(filename, unicode):
                filename = unicode(filename, 'utf-8')
        if stream:
            return filename, response.iter_content(WebAPI.ITER_CHUNK_SIZE)
        return filename, response.content
    def post(self, url, data, **kwargs):
        try:
            response = self.session.post(url, data, cookies=self.cookies, **kwargs)
        except requests.ConnectionError as e:
            raise WebAPIException(CONNECTION_ABORTED)
        except SocketError as e:
            if e.errno == errno.ECONNRESET:
                raise WebAPIException(CONNECTION_ECONNRESET)
            raise e
        if not self.is_success(response.status_code):
            raise WebAPIException(REQUEST_FAILED)
        self.update_cookies()
        return response
    def put(self, url, data=None, **kwargs):
        try:
            kwargs.pop('cookies', None)
            response = self.session.put(url, data=data, cookies=self.cookies, **kwargs)
        except requests.ConnectionError as e:
            raise WebAPIException(CONNECTION_ABORTED)
        except SocketError as e:
            if e.errno == errno.ECONNRESET:
                raise WebAPIException(CONNECTION_ECONNRESET)
            raise e
        if not self.is_success(response.status_code):
            raise WebAPIException(REQUEST_FAILED)
        self.update_cookies()
        return response
    def validate(self):
        pass
    def parse(self, beautiful_html):
        return beautiful_html
    def beautifulsoup(self, html):
        return BeautifulSoup(html, convertEntities=BeautifulSoup.HTML_ENTITIES)
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
        except ValueError as decodingerror:
            raise WebAPIException(JASON_DECODING_FAILURE)
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
            except ValueError as decodingerror:
                raise WebAPIException(JASON_DECODING_FAILURE)
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
            except ValueError as decodingerror:
                raise WebAPIException(JASON_DECODING_FAILURE)
        return response
    def multipart_upload(self, url, data=None, **kwargs):
        self.validate()
        encoder = MultipartEncoder(fields=data)
        response = self.post(url=url, data=encoder,
                             headers={'Content-Type': encoder.content_type,
                                      'Content-Length': encoder.len,
                                     },
                             **kwargs
                            )
        return self.parse(self.beautifulsoup(response.content))
    def show_captcha(self, url):
        _, content_iterator = self.get_file(url)
        imagebytes = bytes().join(content_iterator)
        in_memory_file = StringIO(imagebytes)
        Image.open(in_memory_file).show()