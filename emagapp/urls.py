from django.urls import path
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('category/<str:category_slug>/', views.category_view, name='category_detail'),
    path('product/<str:product_slug>/', views.product_view, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('add_to_cart/', views.add_to_cart_view, name='add_to_cart'),
    path('remove_from_cart/', views.remove_from_cart_view, name='remove_from_cart'),
    path('change_item_qty/', views.change_item_qty, name='change_item_qty'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('order/', views.order_create_view, name='create_order'),
    path('make_order/', views.make_order_view, name='make_order'),
    path('thank_you/', TemplateView.as_view(template_name='emagapp/thank_you.html'), name='thank_you'),
    path('account/', views.account_view, name='account'),
    path('registration/', views.registration_view, name='registration'),
    path('login/', LoginView.as_view(template_name='emagapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
]
