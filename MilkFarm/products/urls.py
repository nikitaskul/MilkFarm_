from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home_page'),
    path('products/', views.ProductsList.as_view(), name='products_list'),
    path('products/<category_slug>/', views.ProductsListByCategory.as_view(), name='products_list_by_category'),
    path('products/<id>/<slug>/', views.ProductDetail.as_view(), name='product_detail')
]
