from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy


class CustomUserManager(BaseUserManager):
    """
    Собственная модель пользователя, где email является идентификатором
    """
    def create_user(self, email, password, **extra_fields):
        """
        Создает и сохраняет пользрователя с заданным email и password и допольнительными полями
        """
        if not email:
            raise ValueError(ugettext_lazy('Users must have an email address'))
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Создает и сохраняет пользователя с заданым email и password и дополнительными полями
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(ugettext_lazy('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(ugettext_lazy('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
