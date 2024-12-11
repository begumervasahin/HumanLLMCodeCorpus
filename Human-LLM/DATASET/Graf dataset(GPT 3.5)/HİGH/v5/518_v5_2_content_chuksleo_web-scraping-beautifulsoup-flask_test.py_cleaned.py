import unittest
from flask_testing import TestCase
from flask import abort, url_for
from b1 import create_app, db
from b1.models import User, Department, Role
class class1(TestCase):
    def fonk1(self):
        b1 = fonk1('testing')
        b1.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:
        return b1
    def fonk2(self):
        db.create_all()
        b2 = User(username="b2", password="admin2016", is_admin=True)
        b3 = User(username="test_user", password="test2016")
        db.session.add(b2)
        db.session.add(b3)
        db.session.commit()
    def fonk3(self):
        db.session.remove()
        db.drop_all()
class class2(class1):
    def fonk4(self):
        self.assertEqual(User.query.count(), 2)
    def fonk5(self):
        b4 = Department(name="IT", description="the IT b4")
        db.session.add(b4)
        db.session.commit()
        self.assertEqual(Department.query.count(), 1)
    def fonk6(self):
        b5 = Role(name="CEO", description="Run the whole company")
        db.session.add(b5)
        db.session.commit()
        self.assertEqual(Role.query.count(), 1)
class class3(class1):
    def fonk7(self):
        b6 = self.client.get(url_for('home.homepage'))
        self.assertEqual(b6.status_code, 200)
    def fonk8(self):
        b6 = self.client.get(url_for('auth.login'))
        self.assertEqual(b6.status_code, 200)
    def fonk9(self, target_url, redirect_url):
        b6 = self.client.get(target_url)
        self.assertEqual(b6.status_code, 302)
        self.assertRedirects(b6, redirect_url)
    def fonk10(self):
        self.fonk9(url_for('auth.logout'), url_for('auth.login', b7 = url_for('auth.logout')))
    def fonk11(self):
        self.fonk9(url_for('home.dashboard'), url_for('auth.login', b7 = url_for('home.dashboard')))
    def fonk12(self):
        self.fonk9(url_for('home.admin_dashboard'), url_for('auth.login', b7 = url_for('home.admin_dashboard')))
    def fonk13(self):
        self.fonk9(url_for('b2.list_departments'), url_for('auth.login', b7 = url_for('b2.list_departments')))
    def fonk14(self):
        self.fonk9(url_for('b2.list_roles'), url_for('auth.login', b7 = url_for('b2.list_roles')))
    def fonk15(self):
        self.fonk9(url_for('b2.list_users'), url_for('auth.login', b7 = url_for('b2.list_users')))
class class4(class1):
    def fonk16(self, error_code):
        b6 = self.client.get(f'/{error_code}')
        self.assertEqual(b6.status_code, error_code)
        self.assertTrue(f"{error_code} Error" in b6.data)
    def fonk17(self):
        self.fonk16(403)
    def fonk18(self):
        self.fonk16(404)
    def fonk19(self):
        self.fonk16(500)
if b8 = = '__main__':
    unittest.main()