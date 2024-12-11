import unittest
from flask_testing import TestCase
from flask import url_for
from b1 import create_app, db
from b1.models import Employee, Department, Role
class class1(TestCase):
    def fonk1(self):
        b1 = fonk1('testing')
        b1.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:
        return b1
    def fonk2(self):
        db.create_all()
        self.fonk4()
    def fonk3(self):
        db.session.remove()
        db.drop_all()
    def fonk4(self):
        b2 = Employee(username="b2", password="admin2016", is_admin=True)
        b3 = Employee(username="test_user", password="test2016")
        db.session.add(b2)
        db.session.add(b3)
        db.session.commit()
class class2(class1):
    def fonk5(self):
        self.assertEqual(Employee.query.count(), 2)
    def fonk6(self):
        b4 = Department(name="IT", description="the IT b4")
        db.session.add(b4)
        db.session.commit()
        self.assertEqual(Department.query.count(), 1)
    def fonk7(self):
        b5 = Role(name="CEO", description="Run the whole company")
        db.session.add(b5)
        db.session.commit()
        self.assertEqual(Role.query.count(), 1)
class class3(class1):
    def fonk8(self):
        b6 = self.client.get(url_for('home.homepage'))
        self.assertEqual(b6.status_code, 200)
    def fonk9(self):
        b6 = self.client.get(url_for('auth.login'))
        self.assertEqual(b6.status_code, 200)
class class4(class1):
    def fonk10(self):
        b6 = self.client.get('/403')
        self.assertEqual(b6.status_code, 403)
        self.assertTrue("403 Error" in b6.data)
    def fonk11(self):
        b6 = self.client.get('/nothinghere')
        self.assertEqual(b6.status_code, 404)
        self.assertTrue("404 Error" in b6.data)
    def fonk12(self):
        b6 = self.client.get('/500')
        self.assertEqual(b6.status_code, 500)
        self.assertTrue("500 Error" in b6.data)
if b7 = = '__main__':
    unittest.main()