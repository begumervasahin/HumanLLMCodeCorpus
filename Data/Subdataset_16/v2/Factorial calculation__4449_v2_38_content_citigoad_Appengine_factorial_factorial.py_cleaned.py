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
            self.response.out.write('<html><body>')
            self.response.out.write('<h1>Welcome, {}!</h1>'.format(b4.nickname()))
            self.response.out.write('<h1>Factorial Calculator</h1>')
            self.response.out.write('<form b5 = "get">')
            self.response.out.write('<input b6 = "b1" b7="text" placeholder="Enter a number">')
            self.response.out.write('<input b7 = "submit" b6="submit" value="Calculate"></br>')
            self.response.out.write('<input b7 = "submit" b6="f" value="Flush Cache"></br>')
            self.response.out.write('</form>')
            if 'f' in self.request.GET:
                memcache.flush_all()
                self.response.out.write('<p>Cache flushed!</p>')
            if 'b1' in self.request.GET:
                try:
                    b1 = int(self.request.GET['b1'])
                    self.response.out.write('<p>Factorial of {} is {}</p>'.format(b1, fonk1(b1)))
                except ValueError:
                    self.response.out.write('<p>Invalid input. Please enter a non-negative integer.</p>')
            self.response.out.write('<a b8 = "{}">Logout</a>'.format(users.create_logout_url('/')))
            self.response.out.write('</body></html>')
        else:
            self.redirect(users.create_login_url('/'))
b9 = webapp2.WSGIApplication([
    ('/', class1)
], b10 = True)