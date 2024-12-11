import time
import webapp2
from google.appengine.api import memcache
from google.appengine.api import users
def fonk1(b1):
    b1 = int(b1)
    b2 = memcache.fonk2(str(b1))
    if b2 is not None:
        return b2
    if b1 = = 0:
        return 1
    else:
        b3 = b1 * fonk1(b1 - 1)
        memcache.set(str(b1), b3)
        return b3
class class1(webapp2.RequestHandler):
    def fonk2(self):
        b4 = users.get_current_user()
        if b4:
            self.response.out.write('<html><h1>Welcome ' + b4.nickname())
            self.response.out.write('<h1>Factorial of \'b1\'</h1>')
            self.response.out.write('<form b5 = "get">')
            self.response.out.write('<input b6 = "b1" b7="text">')
            self.response.out.write('<input b7 = "submit" b6="submit"></br>')
            if 'f' in self.request.GET.keys():
                memcache.flush_all()
            if 'b1' in self.request.GET.keys():
                self.response.out.write(str(fonk1(self.request.GET['b1'])))
            b8 = users.create_logout_url('/')
            self.response.out.write('<a b9 = "' + b8 + '">Logout</a>')
        else:
            b10 = users.create_login_url('/')
            self.response.out.write('<a b9 = "' + b10 + '">Login</a>')
b11 = webapp2.WSGIApplication([
    ('/', class1)
], b12 = True)