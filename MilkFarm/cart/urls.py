from django.urls import path

from . import views


app_name = 'cart'
urlpatterns = [
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('pay/', views.cart_pay, name='cart_pay'),
    path('', views.cart_detail, name='cart_detail'),
]
