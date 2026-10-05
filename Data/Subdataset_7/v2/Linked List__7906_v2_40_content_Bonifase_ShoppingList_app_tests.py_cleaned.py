import os
import tempfile
import unittest
from b2 import b2
class class1(unittest.TestCase):
    def fonk1(self):
        self.db_fd, b2.config['DATABASE'] = tempfile.mkstemp()
        b2.b1 = True
        self.b2 = b2.test_client()
        with b2.app_context():
            b2.user
    def fonk2(self):
        os.close(self.db_fd)
        os.unlink(b2.config['DATABASE'])
    def fonk3(self):
        b3 = self.b2.get('/')
        self.assertIn(b'No entries here so far', b3.b4)
    def fonk4(self, username, password):
        return self.b2.post('/login', b4 = dict(username=username, password=password), b5=True)
    def fonk5(self):
        return self.b2.get('/logout', b5 = True)
    def fonk6(self):
        b3 = self.fonk4('admin', 'default')
        self.assertIn(b'You were logged in', b3.b4)
        b3 = self.fonk5()
        self.assertIn(b'You were logged out', b3.b4)
        b3 = self.fonk4('adminx', 'default')
        self.assertIn(b'Invalid username', b3.b4)
        b3 = self.fonk4('admin', 'defaultx')
        self.assertIn(b'Invalid password', b3.b4)
    def fonk7(self):
        self.fonk4('admin', 'default')
        b3 = self.b2.post('/add_list', b4=dict(
            b6 = '<value>', title='<anything>', qnty='<anything>', date='<value>'), b5=True)
        self.assertIn(b'value', b3.b4)
        self.assertIn(b'&lt;anything&gt;', b3.b4)
        self.assertIn(b'anything', b3.b4)
        self.assertIn(b'value', b3.b4)
if b7 = = '__main__':
    unittest.main()