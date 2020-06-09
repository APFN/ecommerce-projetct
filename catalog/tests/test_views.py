from django.test import TestCase, Client
from catalog.models import Category, Products
from django.urls import reverse

from model_mommy import mommy

class ProductListTestCase(TestCase):
    def setUp(self):
        self.url =reverse('catalog:product_list')
        mommy.make('catalog.Products', _quantity=100)
        self.client = Client()

    def tearDown(self):
        Products.objects.all().delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/product_list.html')

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('product_list' in response.context)
        product_list = response.context['product_list']
        self.assertEquals(product_list.count(), 100)