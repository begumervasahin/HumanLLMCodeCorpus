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
    result = n * factorial(n - 1)
    memcache.set(str(n), result)
    return result
class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        self.response.out.write('<html><body>')
        if user:
            self.response.out.write('<h1>Welcome, {}!</h1>'.format(user.nickname()))
            self.response.out.write('<h1>Factorial Calculator</h1>')
            self.response.out.write('<form method="get">')
            self.response.out.write('<input name="n" type="text" placeholder="Enter a number">')
            self.response.out.write('<input type="submit" value="Calculate">')
            self.response.out.write('<input type="submit" name="f" value="Flush Cache">')
            self.response.out.write('</form>')
            if 'f' in self.request.GET:
                memcache.flush_all()
                self.response.out.write('<p>Cache flushed!</p>')
            if 'n' in self.request.GET:
                try:
                    n = int(self.request.GET['n'])
                    factorial_result = factorial(n)
                    self.response.out.write('<p>Factorial of {} is {}</p>'.format(n, factorial_result))
                except ValueError:
                    self.response.out.write('<p>Invalid input. Please enter a non-negative integer.</p>')
            self.response.out.write('<a href="{}">Logout</a>'.format(users.create_logout_url('/')))
        else:
            self.response.out.write('<a href="{}">Login</a>'.format(users.create_login_url('/')))
        self.response.out.write('</body></html>')
app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)