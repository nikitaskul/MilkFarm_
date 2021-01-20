from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy
from django.utils import timezone

from .managers import CustomUserManager
from . import crypt


class User(AbstractBaseUser, PermissionsMixin):
    """
    Модель кастомизированого пользователя
    """
    email = models.EmailField(gettext_lazy('Email address'), unique=True)

    name = models.CharField(gettext_lazy('Name'), max_length=50, blank=True)
    date_of_birth = models.DateField(gettext_lazy('Birth date'), blank=True, null=True)
    phone_number = models.CharField(gettext_lazy('Phone number'), max_length=30, blank=True)
    address = models.CharField(gettext_lazy('Address'), max_length=150, blank=True)
    about = models.CharField(gettext_lazy('About'), max_length=150, blank=True)
    company = models.CharField(gettext_lazy('Company'), max_length=150, blank=True)
    card_number = models.CharField(gettext_lazy('Card number'), max_length=128, blank=True)
    amount = models.DecimalField(gettext_lazy('Amount'), max_digits=10, decimal_places=2, default=0)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def show_last_card_letters(self):
        """
        Возвращает частичную информацию о карте
        """
        decode_card_number = crypt.decode_card_number(str(self.card_number))
        if decode_card_number != '':
            return '**** **** **** ' + decode_card_number[-4:]
        return ''

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users_user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']
