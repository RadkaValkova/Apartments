import os
from os.path import join

from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from Apart.accounts.models import Profile
from Apart.apart_app.forms import BootstrapFormMixin

UserModel = get_user_model()


class LoginForm(forms.Form):
    user = None
    email = forms.EmailField(
        label='e-mail',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Въведете Вашият e-mail',
                'style': 'width: 450px',
            }
        )
    )
    password = forms.CharField(
        label='Парола',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Въведете паролата си',
                'style': 'width: 300px',
            }
        ),
    )

    def clean_password(self):
        self.user = authenticate(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise ValidationError('Невалидни парола или e-mail')

    def save(self):
        return self.user


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label='Парола',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Въведете паролата си',
                'style': 'width: 500px'
            }
        ),
        help_text='Паролата Ви не може да бъде твърде подобна на другите Ви лични данни. \n '
                  'Паролата Ви трябва да съдържа поне 8 знака.\n'
                  'Паролата Ви не може да бъде често използвана парола.\n'
                  'Паролата Ви не може да бъде изцяло цифрова. \n',
    )
    password2 = forms.CharField(
        label='Потвърждаване на парола',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Моля, въведете повторно паролата',
                'style': 'width: 500px'
            }
        ),
        help_text='Въведете същата парола като преди, за проверка. ',
    )

    class Meta:
        model = UserModel
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Моля, въведете e-mail',
                    'style': 'width: 650px'
                }
            ),
        }


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    # def save(self, commit=True):
    #     db_apart = Profile.objects.get(pk=self.instance.id)
    #     if commit:
    #         image_path = join(settings.MEDIA_ROOT, str(db_apart.image))
    #         os.remove(image_path)
    #     return super().save(commit)

    first_name = forms.CharField(
        label='Име',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Въведете името си',
                'style': 'width: 400px'
            }
        )
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Въведете фамилията си',
                'style': 'width: 400px'
            }
        )
    )
    phone_number = forms.CharField(
        label='Телефон за контакт',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Въведете телефонен номер',
                'style': 'width: 400px'
            }
        )
    )

    class Meta:
        model = Profile
        # fields = '__all__'
        exclude = ('user',)


