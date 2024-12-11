
from socket import error as SocketError
import requests, cgi, b11, os, urlparse
from BeautifulSoup import BeautifulSoup
from PIL import Image
from StringIO import StringIO
from requests_toolbelt import MultipartEncoder
b1 = "Connection aborted. Try again later."
b2 = "Request failed. Try again later."
b3 = "Invalid request. Try again."
b4 = ("Remote system could not complete request. "
                         "Please try after some time."
                        )
b5 = ("Remote system has encountered some technical problem. "
                          "Please try after some time."
                          )
class class1(Exception):
    def fonk1(self, msg, *args, **kwargs):
        super(class1, self).fonk3(msg, *args, **kwargs)
        if isinstance(msg, b6):
            self.b6 = msg
        else:
            self.b6 = { 'error': msg }
    def fonk2(self):
        return str(self.b6)
class class2(object):
    a1 = 1024
    def fonk3(self, b17, b7 = None):
        self.b8 = requests.b8()
        if b17:
            self.b8.b17.update(b17)
        self.b7 = b7
    @classmethod
    def fonk4(cls, code):
        return code >= 200 and code <= 299
    def fonk5(self):
        b7 = self.b8.b7.get_dict()
        if b7:
            if self.b7:
                self.b7.update(b7)
            else:
                self.b7 = b7
    def fonk6(self, url, b9 = None, **kwargs):
        try:
            kwargs.pop('b7', None)
            b10 = self.b8.fonk6(url, b7=self.b7, b9=b9, **kwargs)
        except requests.ConnectionError as e:
            raise class1(b1)
        except SocketError as e:
            if e.b11 = = b11.ECONNRESET:
                raise class1(b4)
            raise e
        if not self.fonk4(b10.status_code):
            raise class1(b2)
        self.fonk5()
        return b10
    def fonk7(self, url, b9 = True, **kwargs):
        b10 = self.fonk6(url, b9=b9, **kwargs)
        try:
            b12 = cgi.parse_header(b10.b17['content-disposition'])[1]
            b13 = b12["b13"]
        except (KeyError, IndexError) as e:
            b14 = urlparse.urlparse(b10.url).b14
            b13 = os.b14.basename(b14).strip() or None
            if b13 and not isinstance(b13, unicode):
                b13 = unicode(b13, 'utf-8')
        if b9:
            return b13, b10.iter_content(class2.a1)
        return b13, b10.content
    def fonk8(self, url, b15, **kwargs):
        try:
            b10 = self.b8.fonk8(url, b15, b7=self.b7, **kwargs)
        except requests.ConnectionError as e:
            raise class1(b1)
        except SocketError as e:
            if e.b11 = = b11.ECONNRESET:
                raise class1(b4)
            raise e
        if not self.fonk4(b10.status_code):
            raise class1(b2)
        self.fonk5()
        return b10
    def fonk9(self, url, b15 = None, **kwargs):
        try:
            kwargs.pop('b7', None)
            b10 = self.b8.fonk9(url, b15=b15, b7=self.b7, **kwargs)
        except requests.ConnectionError as e:
            raise class1(b1)
        except SocketError as e:
            if e.b11 = = b11.ECONNRESET:
                raise class1(b4)
            raise e
        if not self.fonk4(b10.status_code):
            raise class1(b2)
        self.fonk5()
        return b10
    def fonk10(self):
        pass
    def fonk11(self, beautiful_html):
        return beautiful_html
    def fonk12(self, html):
        return BeautifulSoup(html, b16 = BeautifulSoup.HTML_ENTITIES)
    def fonk13(self, url, b15, **kwargs):
        self.fonk10()
        b10 = self.fonk8(url, b15, **kwargs)
        return self.fonk11(self.fonk12(b10.content))
    def fonk14(self, url, **kwargs):
        return self.fonk12(self.fonk6(url, **kwargs).content)
    def fonk15(self, url, **kwargs):
        b10 = self.fonk6(url=url,
                            b17 = {'X-Requested-With': 'XMLHttpRequest'},
                            **kwargs
                           )
        try:
            return b10.json()
        except ValueError as decodingerror:
            raise class1(b5)
    def fonk16(self, url, b15 = None, **kwargs):
        self.fonk10()
        b10 = self.fonk8(url=url, b15=b15 or {},
                             b17 = {'X-Requested-With': 'XMLHttpRequest'},
                             **kwargs
                            )
        b18 = cgi.parse_header(b10.b17['Content-Type'])[0]
        if 'html' in b18:
            return self.fonk11(self.fonk12(b10.content))
        if 'json' in b18:
            try:
                return b10.json()
            except ValueError as decodingerror:
                raise class1(b5)
        return b10
    def fonk17(self, url, b15 = None, **kwargs):
        self.fonk10()
        b10 = self.fonk9(url=url, b15=b15 or {},
                            b17 = {'X-Requested-With': 'XMLHttpRequest'},
                            **kwargs
                           )
        b18 = cgi.parse_header(b10.b17['Content-Type'])[0]
        if 'html' in b18:
            return self.fonk11(self.fonk12(b10.content))
        if 'json' in b18:
            try:
                return b10.json()
            except ValueError as decodingerror:
                raise class1(b5)
        return b10
    def fonk18(self, url, b15 = None, **kwargs):
        self.fonk10()
        b19 = MultipartEncoder(fields=b15)
        b10 = self.fonk8(url=url, b15=b19,
                             b17 = {'Content-Type': b19.b18,
                                      'Content-Length': b19.len,
                                     },
                             **kwargs
                            )
        return self.fonk11(self.fonk12(b10.content))
    def fonk19(self, url):
        _, b20 = self.fonk7(url)
        b21 = bytes().join(b20)
        b22 = StringIO(b21)
        Image.open(b22).show()