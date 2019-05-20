from django.test import TestCase
from emagapp.models import Category, Brand, Product

class CategoryModelTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		Category.objects.create(name='Test', slug='test')

	def test_category_name(self):
		category = Category.objects.get(id=1)
		self.assertEqual(str(category), category.name)

	def test_category_name_max_length(self):
		category = Category.objects.get(id=1)
		max_length = category._meta.get_field('name').max_length
		self.assertEqual(max_length, 100)

	def test_get_absolute_url(self):
		category = Category.objects.get(id=1)
		self.assertEqual(category.get_absolute_url(), '/category/test/')


class BrandModelTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		Brand.objects.create(name='Test')

	def test_brand_name(self):
		brand = Brand.objects.get(id=1)
		self.assertEqual(str(brand), brand.name)

	def test_brand_name_max_length(self):
		brand = Brand.objects.get(id=1)
		max_length = brand._meta.get_field('name').max_length
		self.assertEqual(max_length, 100)


