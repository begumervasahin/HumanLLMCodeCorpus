import os
import unittest
import tempfile
import app
class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.testing = True
        self.app = app.app.test_client()
        with app.app.app_context():
            app.init_db()
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])
    def test_empty_db(self):
        response = self.app.get('/')
        self.assertIn(b'No entries here so far', response.data)
    def login(self, username, password):
        return self.app.post('/login', data=dict(username=username, password=password), follow_redirects=True)
    def logout(self):
        return self.app.get('/logout', follow_redirects=True)
    def test_login_logout(self):
        response = self.login('admin', 'default')
        self.assertIn(b'You were logged in', response.data)
        response = self.logout()
        self.assertIn(b'You were logged out', response.data)
        response = self.login('adminx', 'default')
        self.assertIn(b'Invalid username', response.data)
        response = self.login('admin', 'defaultx')
        self.assertIn(b'Invalid password', response.data)
    def test_lists(self):
        self.login('admin', 'default')
        response = self.app.post('/add_list', data=dict(
            id='<value>', title='<anything>', qnty='<anything>', date='<value>'), follow_redirects=True)
        self.assertIn(b'<value>', response.data)
        self.assertIn(b'&lt;anything&gt;', response.data)
        self.assertIn(b'anything', response.data)
        self.assertIn(b'<value>', response.data)
if __name__ == '__main__':
    unittest.main()