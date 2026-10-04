import os
import app
import unittest
import tempfile
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
            id='1', title='Sample Title', qnty='10', date='2024-07-27'), follow_redirects=True)
        self.assertIn(b'1', rv.data)
        self.assertIn(b'Sample Title', rv.data)
        self.assertIn(b'10', rv.data)
        self.assertIn(b'2024-07-27', rv.data)
if __name__ == '__main__':
    unittest.main()