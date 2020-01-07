from django.forms import TextInput, ModelForm
from .models import User

class UserFormRegister(ModelForm):
    class Meta:
        model = login
        second_model = password
        fields = ['login', 'password']
        widgets = {'login' = TextInput(attrs={
            'class': 'form-control',
            'name': 'login',
            'id': 'login',
            'placeholder': 'Введите ваш логин' 
        }),
        'password' = TextInput(attrs={
            'class': 'form-control',
            'name': 'password',
            'id': 'password',
            'placeholder': 'Придумайте ваш пароль' 
        })
        }