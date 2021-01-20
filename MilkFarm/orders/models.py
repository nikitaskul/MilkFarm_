from django.db import models
import decimal

from products.models import Product


class Order(models.Model):

    name = models.CharField(max_length=50, verbose_name='Имя заказчика')
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(max_length=150, verbose_name='Адрес доставки')
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f'Заказ {self.pk}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.pk}'

    def get_cost(self):
        return self.price * self.quantity
