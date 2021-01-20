from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product
from cart.forms import CartAddProductForm


def index(request):
    return render(request, 'products/index.html')


class ProductsList(ListView):
    """
    Отображает все доступные продукты на странице поиска продуктов
    """
    model = Product
    template_name = 'products/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsList, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Product.objects.filter(available=True)


class ProductsListByCategory(ListView):
    """
    Отображает список всех доступных продуктов по категориям
    """
    model = Product
    template_name = 'products/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListByCategory, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Product.objects.filter(category_id__slug=self.kwargs['category_slug'], available=True)


class ProductDetail(DetailView):
    """
    Отображает детали конкретного продукта
    """
    model = Product
    template_name = 'products/product_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context
