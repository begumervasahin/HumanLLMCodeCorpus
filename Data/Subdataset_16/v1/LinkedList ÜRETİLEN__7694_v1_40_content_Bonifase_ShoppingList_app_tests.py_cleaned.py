import os
import unittest
import tempfile
from b1 import b1
class class1(unittest.TestCase):
    def fonk1(self):
        self.db_fd, b1.config['DATABASE'] = tempfile.mkstemp()
        b1.config['TESTING'] = True
        self.b1 = b1.test_client()
        with b1.app_context():
            b1.init_db()
    def fonk2(self):
        os.close(self.db_fd)
        os.unlink(b1.config['DATABASE'])
    def fonk3(self):
        b2 = self.b1.get('/')
        assert b'No entries here so far' in b2.b3
    def fonk4(self, username, password):
        return self.b1.post('/login', b3 = dict(username=username, password=password), b4=True)
    def fonk5(self):
        return self.b1.get('/logout', b4 = True)
    def fonk6(self):
        b2 = self.fonk4('admin', 'default')
        assert b'You were logged in' in b2.b3
        b2 = self.fonk5()
        assert b'You were logged out' in b2.b3
        b2 = self.fonk4('adminx', 'default')
        assert b'Invalid username' in b2.b3
        b2 = self.fonk4('admin', 'defaultx')
        assert b'Invalid password' in b2.b3
    def fonk7(self):
        self.fonk4('admin', 'default')
        b2 = self.b1.post('/add_list', b3=dict(
            b5 = '1', title='Test Title', qnty='10', date='2024-07-27'), b4=True)
        assert b'1' in b2.b3
        assert b'Test Title' in b2.b3
        assert b'10' in b2.b3
        assert b'2024-07-27' in b2.b3
if b6 = = '__main__':
    unittest.main()