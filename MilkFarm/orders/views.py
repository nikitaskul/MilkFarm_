from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


@login_required
@transaction.atomic
def order_create(request):
    cart = Cart(request)
    user = request.user
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            if order.paid:
                if user.amount - cart.get_total_price() > 0:
                    user.amount = user.amount - cart.get_total_price()
                    user.save()
                    messages.success(request, 'Товар успешно оплачен')
                else:
                    messages.warning(request, 'Недостаточно денег на счету')
                    return render(request, 'orders/order/fail.html', {'order': order})
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
