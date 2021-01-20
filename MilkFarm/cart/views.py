from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from products.models import Product

from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    if cart.cart[str(product_id)]['quantity'] > product.stock:
        cart.cart[str(product_id)]['quantity'] = product.stock
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


@login_required
@transaction.atomic
def cart_pay(request):
    cart = Cart(request)
    user = request.user
    if user.amount - cart.get_total_price() > 0:
        user.amount = user.amount - cart.get_total_price()
        user.save()
        cart.clear()
        messages.success(request, 'Товар успешно оплачен')
    else:
        messages.warning(request, 'Недостаточно денег на счету')
    return render(request, 'cart/success.html')
