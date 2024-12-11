import os
import b2
import unittest
import tempfile
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
        assert 'No entries here so far'
    def fonk4(self, username, password):
        return self.b2.post('/login', b4 = dict(username=username,password=password), b5=True)
    def fonk5(self):
        return self.b2.get('/logout', b5 = True)
    def fonk6(self):
        b3 = self.fonk4('admin', 'default')
        assert 'You were logged in'
        b3 = self.fonk5()
        assert 'You were logged out'
        b3 = self.fonk4('adminx', 'default')
        assert 'Invalid username'
        b3 = self.fonk4('admin', 'defaultx')
        assert 'Invalid password'
    def fonk7(self):
        self.fonk4('admin', 'default')
        b3 = self.b2.post('/add_list', b4=dict(
        b6 = '<value>', title='<anything>', qnty='<anything>', date='<value>'), b5=True)
        assert 'value'
        assert '&lt;anything&gt;'
        assert 'anything'
        assert 'value'
if b7 = = '__main__':
    unittest.main()