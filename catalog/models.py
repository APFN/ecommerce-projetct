from django.db import models

class Category(models.Model):
    name= models.CharField('Name', max_length=100)
    slug = models.SlugField('Identifier', max_length=100)
    created = models.DateTimeField('Created in', auto_now_add=True)
    modified = models.DateTimeField('Modified in', auto_now=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

class Products(models.Model):
    name= models.CharField('Name', max_length=100)
    slug = models.SlugField('Identifier', max_length=100)
    category = models.ForeignKey('catalog.Category', verbose_name='Category', on_delete=models.CASCADE)
    description = models.TextField('Description', blank=True)
    price = models.DecimalField('Price', decimal_places=2, max_digits=10)

    created = models.DateTimeField('Created in', auto_now_add=True)
    modified = models.DateTimeField('Modified in', auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']