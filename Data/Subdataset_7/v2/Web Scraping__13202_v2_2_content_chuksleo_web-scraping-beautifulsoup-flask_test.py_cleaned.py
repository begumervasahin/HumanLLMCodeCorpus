import unittest
from flask_testing import TestCase
from flask import abort, url_for
from b2 import create_app, db
from b2.models import Employee, Department, Role
class class1(TestCase):
    def fonk1(self):
        b1 = 'testing'
        b2 = fonk1(b1)
        b2.config.update(b3 = 'sqlite:
        return b2
    def fonk2(self):
        db.create_all()
        b4 = Employee(username="b4", password="admin2016", is_admin=True)
        b5 = Employee(username="test_user", password="test2016")
        db.session.add(b4)
        db.session.add(b5)
        db.session.commit()
    def fonk3(self):
        db.session.remove()
        db.drop_all()
class class2(class1):
    def fonk4(self):
        self.assertEqual(Employee.query.count(), 2)
    def fonk5(self):
        b6 = Department(name="IT", description="the IT b6")
        db.session.add(b6)
        db.session.commit()
        self.assertEqual(Department.query.count(), 1)
    def fonk6(self):
        b7 = Role(name="CEO", description="Run the whole company")
        db.session.add(b7)
        db.session.commit()
        self.assertEqual(Role.query.count(), 1)
class class3(class1):
    def fonk7(self):
        b8 = self.client.get(url_for('home.homepage'))
        self.assertEqual(b8.status_code, 200)
    def fonk8(self):
        b8 = self.client.get(url_for('auth.login'))
        self.assertEqual(b8.status_code, 200)
class class4(class1):
    def fonk9(self):
        b8 = self.client.get('/403')
        self.assertEqual(b8.status_code, 403)
        self.assertTrue("403 Error" in b8.data)
    def fonk10(self):
        b8 = self.client.get('/nothinghere')
        self.assertEqual(b8.status_code, 404)
        self.assertTrue("404 Error" in b8.data)
    def fonk11(self):
        b8 = self.client.get('/500')
        self.assertEqual(b8.status_code, 500)
        self.assertTrue("500 Error" in b8.data)
if b9 = = '__main__':
    unittest.main()