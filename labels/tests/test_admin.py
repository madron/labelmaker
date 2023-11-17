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
        obj = factories.StyleFactory()
        url = reverse('admin:labels_style_change', args=(obj.pk,))
        with self.assertNumQueries(5):
            response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        obj = factories.StyleFactory()
        url = reverse('admin:labels_style_delete', args=(obj.pk,))
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
        obj = factories.LabelFactory()
        url = reverse('admin:labels_label_change', args=(obj.pk,))
        with self.assertNumQueries(7):
            response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        obj = factories.LabelFactory()
        url = reverse('admin:labels_label_delete', args=(obj.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class TemplateAdminTest(TestCase):
    def setUp(self):
        UserFactory(username='admin')
        self.assertTrue(self.client.login(username='admin', password='pass'))
        self.list = reverse('admin:labels_template_changelist')

    def test_list(self):
        with self.assertNumQueries(5):
            response = self.client.get(self.list)
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        data = dict(q='text')
        response = self.client.get(self.list, data)
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        url = reverse('admin:labels_template_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        obj = factories.TemplateFactory()
        url = reverse('admin:labels_template_change', args=(obj.pk,))
        with self.assertNumQueries(5):
            response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        obj = factories.TemplateFactory()
        url = reverse('admin:labels_template_delete', args=(obj.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
