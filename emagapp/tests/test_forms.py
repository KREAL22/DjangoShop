from django.test import TestCase
from emagapp.forms import OrderForm

class OrderFormTest(TestCase):

	def test_order_form_name_field_label(self):
		form = OrderForm()
		self.assertEqual(form.fields['name'].label, 'Имя')

	def test_order_form_last_name_field_label(self):
		form = OrderForm()
		self.assertEqual(form.fields['last_name'].label, 'Фамилия')

	def test_order_form_phone_field_label(self):
		form = OrderForm()
		self.assertEqual(form.fields['phone'].label, 'Контактный телефон')

	def test_order_form_buying_type_field_label(self):
		form = OrderForm()
		self.assertEqual(form.fields['buying_type'].label, 'Способ получения')

	def test_order_form_address_field_label(self):
		form = OrderForm()
		self.assertEqual(form.fields['address'].label, 'Адрес доставки')

	def test_order_form_address_field_help_text(self):
		form = OrderForm()
		self.assertEqual(form.fields['address'].help_text, 'Обязательно указывайте город!')

	def test_order_form_comments_field_label(self):
		form = OrderForm()
		self.assertEqual(form.fields['comments'].label, 'Комментарии к заказу')

	def test_order_form_date_field_label(self):
		form = OrderForm()
		self.assertEqual(form.fields['date'].label, 'Дата доставки')

	def test_order_form_date_field_help_text(self):
		form = OrderForm()
		self.assertEqual(form.fields['date'].help_text, 'Доставка производится на следующий день после совершения заказа.')			

       