import unittest
from flask_testing import TestCase
from flask import url_for
from app import create_app, db
from app.models import Employee, Department, Role
class TestBase(TestCase):
    def create_app(self):
        app = create_app('testing')
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:
        return app
    def setUp(self):
        db.create_all()
        self.create_sample_data()
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    def create_sample_data(self):
        admin = Employee(username="admin", password="admin2016", is_admin=True)
        employee = Employee(username="test_user", password="test2016")
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()
class TestModels(TestBase):
    def test_user_model(self):
        self.assertEqual(Employee.query.count(), 2)
    def test_department_model(self):
        department = Department(name="IT", description="the IT department")
        db.session.add(department)
        db.session.commit()
        self.assertEqual(Department.query.count(), 1)
    def test_role_model(self):
        role = Role(name="CEO", description="Run the whole company")
        db.session.add(role)
        db.session.commit()
        self.assertEqual(Role.query.count(), 1)
class TestViews(TestBase):
    def test_homepage_view(self):
        response = self.client.get(url_for('home.homepage'))
        self.assertEqual(response.status_code, 200)
    def test_login_view(self):
        response = self.client.get(url_for('auth.login'))
        self.assertEqual(response.status_code, 200)
class TestErrorPages(TestBase):
    def test_403_forbidden(self):
        response = self.client.get('/403')
        self.assertEqual(response.status_code, 403)
        self.assertTrue("403 Error" in response.data)
    def test_404_not_found(self):
        response = self.client.get('/nothinghere')
        self.assertEqual(response.status_code, 404)
        self.assertTrue("404 Error" in response.data)
    def test_500_internal_server_error(self):
        response = self.client.get('/500')
        self.assertEqual(response.status_code, 500)
        self.assertTrue("500 Error" in response.data)
if __name__ == '__main__':
    unittest.main()