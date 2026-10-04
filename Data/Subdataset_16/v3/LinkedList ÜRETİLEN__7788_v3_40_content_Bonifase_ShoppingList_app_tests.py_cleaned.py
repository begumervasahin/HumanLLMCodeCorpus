import os
import unittest
import tempfile
from app import app
class class1(unittest.TestCase):
    def fonk1(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.b1 = app.test_client()
        with app.app_context():
            app.init_db()
    def fonk2(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])
    def fonk3(self):
        b2 = self.b1.get('/')
        self.assertIn(b'No entries here so far', b2.b3)
    def fonk4(self, b4, b5):
        return self.b1.post('/login', b3 = dict(
            b4 = b4,
            b5 = b5
        ), b6 = True)
    def fonk5(self):
        return self.b1.get('/logout', b6 = True)
    def fonk6(self):
        b2 = self.fonk4('admin', 'default')
        self.assertIn(b'You were logged in', b2.b3)
        b2 = self.fonk5()
        self.assertIn(b'You were logged out', b2.b3)
        b2 = self.fonk4('adminx', 'default')
        self.assertIn(b'Invalid b4', b2.b3)
        b2 = self.fonk4('admin', 'defaultx')
        self.assertIn(b'Invalid b5', b2.b3)
    def fonk7(self):
        self.fonk4('admin', 'default')
        b2 = self.b1.post('/add_list', b3=dict(
            b7 = '1',
            b8 = 'Test Title',
            b9 = '10',
            b10 = '2024-07-27'
        ), b6 = True)
        self.assertIn(b'1', b2.b3)
        self.assertIn(b'Test Title', b2.b3)
        self.assertIn(b'10', b2.b3)
        self.assertIn(b'2024-07-27', b2.b3)
if b11 = = '__main__':
    unittest.main()