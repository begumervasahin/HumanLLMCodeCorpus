import unittest
from flask_testing import TestCase
from flask import abort, url_for
from app import create_app, db
from app.models import User, Department, Role
class TestBase(TestCase):
    def create_app(self):
        app = create_app('testing')
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:
        return app
    def setUp(self):
        db.create_all()
        admin = User(username="admin", password="admin2016", is_admin=True)
        employee = User(username="test_user", password="test2016")
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()
    def tearDown(self):
        db.session.remove()
        db.drop_all()
class TestModels(TestBase):
    def test_user_model(self):
        self.assertEqual(User.query.count(), 2)
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
    def test_redirect_to_login(self, target_url, redirect_url):
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)
    def test_logout_view(self):
        self.test_redirect_to_login(url_for('auth.logout'), url_for('auth.login', next=url_for('auth.logout')))
    def test_dashboard_view(self):
        self.test_redirect_to_login(url_for('home.dashboard'), url_for('auth.login', next=url_for('home.dashboard')))
    def test_admin_dashboard_view(self):
        self.test_redirect_to_login(url_for('home.admin_dashboard'), url_for('auth.login', next=url_for('home.admin_dashboard')))
    def test_departments_view(self):
        self.test_redirect_to_login(url_for('admin.list_departments'), url_for('auth.login', next=url_for('admin.list_departments')))
    def test_roles_view(self):
        self.test_redirect_to_login(url_for('admin.list_roles'), url_for('auth.login', next=url_for('admin.list_roles')))
    def test_user_view(self):
        self.test_redirect_to_login(url_for('admin.list_users'), url_for('auth.login', next=url_for('admin.list_users')))
class TestErrorPages(TestBase):
    def test_error_page(self, error_code):
        response = self.client.get(f'/{error_code}')
        self.assertEqual(response.status_code, error_code)
        self.assertTrue(f"{error_code} Error" in response.data)
    def test_403_forbidden(self):
        self.test_error_page(403)
    def test_404_not_found(self):
        self.test_error_page(404)
    def test_500_internal_server_error(self):
        self.test_error_page(500)
if __name__ == '__main__':
    unittest.main()