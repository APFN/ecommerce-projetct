from django.test import TestCase
from catalog.models import Category, Products
from django.urls import reverse

from model_mommy import mommy

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = mommy.make('catalog.Category')

    def test_get_absolute_url(self):
        self.assertEquals(
            self.category.get_absolute_url(),
            reverse('catalog:category', kwargs={'slug': self.category.slug})
            )

class ProductTestCase(TestCase):
    def setUp(self):
        self.product = mommy.make(Products, slug= 'product')

    def test_get_absolute_url(self):
        self.assertEquals(
            self.product.get_absolute_url(),
            reverse('catalog:product', kwargs={'slug': 'product'})
            )
