from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('change/', views.user_account_change_form, name='change_user_email'),
    path('change_additional_info/', views.user_additional_info_change_form, name='change_additional_info'),
    path('change_payment_details/', views.user_payment_details_change_form, name='change_payment_details'),
    path('add_money/', views.add_money_to_user, name='add_money'),
    path('password/', views.change_password, name='change_password'),
    path('', views.user_account, name='account'),
]
