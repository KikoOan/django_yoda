from django.test import TestCase
from django.urls import reverse, resolve
from . import views

class UrlsTestCase(TestCase):
    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home)

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, views.login)

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, views.logout)

    # Add more test cases for other URLs in your project

    # BEGIN: Add your test cases here

    # END: Add your test cases here