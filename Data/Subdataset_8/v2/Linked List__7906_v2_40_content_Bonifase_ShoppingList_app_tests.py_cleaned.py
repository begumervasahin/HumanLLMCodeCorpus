import os
import tempfile
import unittest
from app import app
class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.testing = True
        self.app = app.test_client()
        with app.app_context():
            app.user
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])
    def test_empty_db(self):
        rv = self.app.get('/')
        self.assertIn(b'No entries here so far', rv.data)
    def login(self, username, password):
        return self.app.post('/login', data=dict(username=username, password=password), follow_redirects=True)
    def logout(self):
        return self.app.get('/logout', follow_redirects=True)
    def test_login_logout(self):
        rv = self.login('admin', 'default')
        self.assertIn(b'You were logged in', rv.data)
        rv = self.logout()
        self.assertIn(b'You were logged out', rv.data)
        rv = self.login('adminx', 'default')
        self.assertIn(b'Invalid username', rv.data)
        rv = self.login('admin', 'defaultx')
        self.assertIn(b'Invalid password', rv.data)
    def test_lists(self):
        self.login('admin', 'default')
        rv = self.app.post('/add_list', data=dict(
            id='<value>', title='<anything>', qnty='<anything>', date='<value>'), follow_redirects=True)
        self.assertIn(b'value', rv.data)
        self.assertIn(b'&lt;anything&gt;', rv.data)
        self.assertIn(b'anything', rv.data)
        self.assertIn(b'value', rv.data)
if __name__ == '__main__':
    unittest.main()