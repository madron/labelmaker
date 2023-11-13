from django.test import TestCase
from django.urls import reverse

from .factories import UserFactory


class HomeAdmin(TestCase):

    def setUp(self):
        UserFactory(username='admin')
        self.assertTrue(self.client.login(username='admin', password='pass'))
        self.list = reverse('admin:index')

    def test_home(self):
        response = self.client.get(self.list)
        self.assertEqual(response.status_code, 200)
