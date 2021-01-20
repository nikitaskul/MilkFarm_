from django.db import models

# from users.models import CustomUser
# from flights.models import Flight
#
#
# class CartProduct(models.Model):
#
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Покупатель')
#     cart = models.ForeignKey('Cart', on_delete=models.CASCADE, verbose_name='Корзина')
#     product = models.ForeignKey(Flight, on_delete=models.CASCADE, verbose_name='Товар')
#     quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Общая цена')
#
#     def __str__(self):
#         return f'{self.product}'
#
#
# class Cart(models.Model):
#