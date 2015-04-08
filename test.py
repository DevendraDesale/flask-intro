from app import app
import unittest


class FlaskTestCase(unittest.TestCase):
    """
    This test class will check for the site login functionality
    """

    def test_index(self):
        """
        Ensure that flask is correctly configured
        """
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_page_loads(self):
        """
        Ensure that flask giving loging page correctly
        """
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)

    def test_correct_login(self):
        """
        Ensure login page works correctly given correct credentials
        """
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username='admin', password='admin'),
            follow_redirects=True
        )
        self.assertIn(b'You have just logged in!', response.data)

    def test_incorrect_login(self):
        """
        Ensure login page works correctly given incorrect credentials
        """
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username='wrong', password='admin'),
            follow_redirects=True
        )
        self.assertIn(b'Invalid credentials, Please try again.', response.data)

    def test_logout(self):
        """
        Ensure logout works correctly
        """
        tester = app.test_client(self)
        tester.post(
            '/login',
            data=dict(username='admin', password='admin'),
            follow_redirects=True
        )
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You have just logged out!', response.data)

    def test_main_route_requires_login(self):
        """
        Ensure that the main page required for the login.
        """
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertTrue(b'You need to login first.' in response.data)

    def test_post_show_up(self):
        """
        Ensure login page works correctly given incorrect credentials
        """
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username='admin', password='admin'),
            follow_redirects=True
        )
        self.assertIn(b"m Hello", response.data)

if __name__ == '__main__':
    unittest.main()
