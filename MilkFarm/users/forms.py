from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User
from . import crypt


class CustomUserCreationForm(UserCreationForm):
    """
    Форма создания пользователя для кастомного пользователя
    """
    def __init__(self, *args, **kwargs):
        """
        Инициализация и редактирование данных, если они существуют.
        """
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.instance.card_number = crypt.decode_card_number(self.instance.card_number)

        # Отдаем новый экземпляр в форму
        kwargs['instance'] = self.instance
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

    class Meta(UserCreationForm):
        model = User
        fields = ('email',)

    def clean_card_number(self):
        """
        Подготовка данных карты к записи в базу данных
        """
        return crypt.encode_card_number(self.cleaned_data['card_number'])


class CustomUserChangeForm(UserChangeForm):
    """
    Форма изменения кастомного пользователя
    """
    def __init__(self, *args, **kwargs):
        """
        Инициализация и редактирование данных, если они существуют.
        """
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

        self.instance.card_number = crypt.decode_card_number(self.instance.card_number)

        # Отдаем новый экземпляр в форму
        kwargs['instance'] = self.instance
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('email',)

    def clean_card_number(self):
        return crypt.encode_card_number(self.cleaned_data['card_number'])
