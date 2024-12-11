import os
import unittest
import tempfile
import b2
class class1(unittest.TestCase):
    def fonk1(self):
        self.db_fd, b2.b2.config['DATABASE'] = tempfile.mkstemp()
        b2.b2.b1 = True
        self.b2 = b2.b2.test_client()
        with b2.b2.app_context():
            b2.user
    def fonk2(self):
        os.close(self.db_fd)
        os.unlink(b2.b2.config['DATABASE'])
    def fonk3(self):
        b3 = self.b2.get('/')
        assert 'No entries here so far' in b3.b4
    def fonk4(self, username, password):
        return self.b2.post('/login', b4 = dict(username=username, password=password), b5=True)
    def fonk5(self):
        return self.b2.get('/logout', b5 = True)
    def fonk6(self):
        b3 = self.fonk4('admin', 'default')
        assert 'You were logged in' in b3.b4
        b3 = self.fonk5()
        assert 'You were logged out' in b3.b4
        b3 = self.fonk4('adminx', 'default')
        assert 'Invalid username' in b3.b4
        b3 = self.fonk4('admin', 'defaultx')
        assert 'Invalid password' in b3.b4
    def fonk7(self):
        self.fonk4('admin', 'default')
        b3 = self.b2.post('/add_list', b4=dict(
            b6 = '<value>', title='<anything>', qnty='<anything>', date='<value>'), b5=True)
        assert '<value>' in b3.b4
        assert '&lt;anything&gt;' in b3.b4
        assert 'anything' in b3.b4
        assert '<value>' in b3.b4
if b7 = = '__main__':
    unittest.main()