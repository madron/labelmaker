from django.test import TestCase
from django.urls import reverse
from . import factories
from authentication.tests.factories import UserFactory


class StyleAdminTest(TestCase):
    def setUp(self):
        UserFactory(username='admin')
        self.assertTrue(self.client.login(username='admin', password='pass'))
        self.list = reverse('admin:labels_style_changelist')

    def test_list(self):
        with self.assertNumQueries(5):
            response = self.client.get(self.list)
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        data = dict(q='text')
        response = self.client.get(self.list, data)
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        url = reverse('admin:labels_style_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        shipment = factories.StyleFactory()
        url = reverse('admin:labels_style_change', args=(shipment.pk,))
        with self.assertNumQueries(5):
            response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        shipment = factories.StyleFactory()
        url = reverse('admin:labels_style_delete', args=(shipment.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class LabelAdminTest(TestCase):
    def setUp(self):
        UserFactory(username='admin')
        self.assertTrue(self.client.login(username='admin', password='pass'))
        self.list = reverse('admin:labels_label_changelist')

    def test_list(self):
        with self.assertNumQueries(5):
            response = self.client.get(self.list)
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        data = dict(q='text')
        response = self.client.get(self.list, data)
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        url = reverse('admin:labels_label_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        shipment = factories.LabelFactory()
        url = reverse('admin:labels_label_change', args=(shipment.pk,))
        with self.assertNumQueries(6):
            response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        shipment = factories.LabelFactory()
        url = reverse('admin:labels_label_delete', args=(shipment.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
