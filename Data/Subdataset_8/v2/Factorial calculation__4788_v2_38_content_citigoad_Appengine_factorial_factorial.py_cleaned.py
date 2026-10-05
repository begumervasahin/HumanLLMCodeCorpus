import time
import webapp2
from google.appengine.api import memcache
from google.appengine.api import users
def factorial(n):
    n = int(n)
    cached_factorial = memcache.get(str(n))
    if cached_factorial is not None:
        return cached_factorial
    if n == 0:
        return 1
    else:
        result = n * factorial(n - 1)
        memcache.set(str(n), result)
        return result
class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.out.write('<html><h1>Welcome ' + user.nickname())
            self.response.out.write('<h1>Factorial of \'n\'</h1>')
            self.response.out.write('<form method="get">')
            self.response.out.write('<input name="n" type="text">')
            self.response.out.write('<input type="submit" name="submit"></br>')
            if 'f' in self.request.GET.keys():
                memcache.flush_all()
            if 'n' in self.request.GET.keys():
                self.response.out.write(str(factorial(self.request.GET['n'])))
            self.response.out.write('<a href="' + users.create_logout_url('/'))
            self.response.out.write('"style="color: blue;">Logout</a>')
        else:
            self.response.out.write('<a href="' + users.create_login_url('/'))
            self.response.out.write('">Login</a>')
app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)