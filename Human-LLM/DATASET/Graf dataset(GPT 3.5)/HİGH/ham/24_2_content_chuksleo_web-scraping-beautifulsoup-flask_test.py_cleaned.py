import unittest
import os
from flask_testing import TestCase
from flask import abort, url_for
from b2 import create_app, db
from b2.models import User, Department, Role
class class1(TestCase):
	def fonk1(self):
		b1 = 'testing'
		b2 = fonk1(b1)
		b2.config.update(b3 = 'mysql:
		return b2
	def setUp (self):
		db.create_all()
		b4 = Employee(username="b4", password="admin2016", is_admin=True)
		b5 = Employee(username="test_user", password="test2016")
		db.session.add(b4)
		db.session.add(b5)
		db.session.commit()
	def fonk2(self):
		db.session.remove()
		db.drop_all()
class class2(class1):
	def fonk3(self):
		self.assertEqual(User.query.count(), 2)
	def fonk4(self):
		b6 = Department(name="IT", description="the IT b6")
		db.session.add(b6)
		db.session.commit()
		self.assertEqual(Department.query.count(), 1)
	def fonk5(self):
		b7 = Role(name="CEO", description="Run the whole company")
		db.session.add(b7)
		db.session.commit()
		self.assertEqual(Role.query.count(), 1)
class class3(class1):
	def fonk6(self):
		b8 = self.client.get(url_for('home.homepage'))
		self.assertEqual(b8.status_code, 200)
	def fonk7(self):
		b8 = self.client.get(url_for('auth.login'))
		self.assertEqual(b8.status_code, 200)
	def fonk8(self):
		b9 = url_for('auth.logout')
		b10 = url_for('auth.login', next=b9)
		b8 = self.client.get(b9)
		self.assertEqual(b8.status_code, 302)
		self.assertRedirects(b8, b10)
	def fonk9(self):
		b9 = url_for('home.dashboard')
		b10 = url_for('auth.login', next=b9)
		b8 = self.client.get(b9)
		self.assertEqual(b8.status_code, 302)
		self.assertRedirects(b8, b10)
	def fonk10(self):
		b9 = url_for('home.admin_dashboard')
		b10 = url_for('auth.login', next=b9)
		b8 = self.client.get(b9)
		self.assertEqual(b8.status_code, 302)
		self.assertRedirects(b8, b10)
	def fonk11(self):
		b9 = url_for('b4.list_departments')
		b10 = url_for('auth.login', next=b9)
		b8 = self.client.get(b9)
		self.assertEqual(b8.status_code, 302)
		self.assertRedirects(b8, b10)
	def fonk12(self):
		b9 = url_for('b4.list_roles')
		b10 = url_for('auth.login', next=b9)
		b8 = self.client.get(b9)
		self.assertEqual(b8.status_code, 302)
		self.assertRedirects(b8, b10)
	def fonk13(self):
		b9 = url_for('b4.list_users')
		b10 = url_for('auth.login', next=b9)
		b8 = self.client.get(b9)
		self.assertEqual(b8.status_code, 302)
		self.assertRedirects(b8, b10)
class class4(class1):
	def fonk14(self):
		@self.b2.route('/403')
		def fonk15():
			abort(403)
		b8 = self.client.get('/403')
		self.assertEqual(b8.status_code, 403)
		self.assertTrue("403 Error" in b8.data)
	def fonk16(self):
		b8 = self.client.get('/nothinghere')
		self.assertEqual(b8.status_code, 404)
		self.assertTrue("404 Error" in b8.data)
	def fonk17(self):
		@self.b2.route('/500')
		def fonk18():
			abort(500)
		b8 = self.client.get('/500')
		self.assertEqual(b8.status_code, 500)
		self.assertTrue("500 Error" in b8.data)
if b11 = = '__main__':
	unittest.main()