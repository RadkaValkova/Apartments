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
            }
        )
    )
    password = forms.CharField(
        label='Парола',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Въведете паролата си',
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
                'placeholder': 'Въведете парола',
                'style': 'width: 300px'
            }
        ),
    )
    password2 = forms.CharField(
        label='Потвърждаване на парола',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Въведете повторно паролата си',
                'style': 'width: 300px'
            }
        ),
    )

    class Meta:
        model = UserModel
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Моля, въведете e-mail',
                    'style': 'width: 500px'
                }
            ),
        }


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    def save(self, commit=True):
        db_profile = Profile.objects.get(pk=self.instance.pk)
        new_image = self.files.get('profile_image')
        old_image = str(db_profile.profile_image)
        old_image_path = os.path.join(settings.MEDIA_ROOT,old_image)
        if commit and new_image and old_image:
            os.remove(old_image_path)
        return super().save(commit=commit)

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

    # profile_image = forms.ImageField(
    #     label='Профилна снимка',
    #     widget=forms.FileInput,
    # )

    class Meta:
        model = Profile
        # fields = '__all__'
        exclude = ('user',)


