from django.test import TestCase
from emagapp.models import Category
from django.urls import reverse

class TestViews(TestCase):

	@classmethod
	def setUpTestData(cls):
		Category.objects.create(name='Test', slug='test')

	def test_category_view(self):
		resp = self.client.get('/category/test/')
		self.assertEqual(resp.status_code, 200)

	def test_home_view(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)	

	def test_reverse_home_view(self):
		resp = self.client.get(reverse('home'))
		self.assertEqual(resp.status_code, 200)

	def test_login_view(self):
		resp = self.client.get('/login/')
		self.assertEqual(resp.status_code, 200)	

	def test_reverse_login_view(self):
		resp = self.client.get(reverse('login'))
		self.assertEqual(resp.status_code, 200)

	def test_registration_view(self):
		resp = self.client.get('/registration/')
		self.assertEqual(resp.status_code, 200)	

	def test_reverse_registration_view(self):
		resp = self.client.get(reverse('registration'))
		self.assertEqual(resp.status_code, 200)			