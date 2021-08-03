
from django.test import TestCase

from Apart.accounts.forms import RegisterForm
from Apart.accounts.models import ApartUser


class RegisterFormTestCase(TestCase):

    def test_whenPasswordsDoesNotMatch_expectRaiseValidationError(self):
        user_form = RegisterForm(
            {'email': 'radka@abv.bg',
             'password1': 'parolata123',
             'password2': 'parolata111'}
        )
        self.assertFalse(user_form.is_valid())

    def test_whenEmailNotValid_expectRaiseValidationError(self):
        user_form = RegisterForm(
            {'email': 'radkaabv.bg',
             'password1': 'parolata123',
             'password2': 'parolata123'}
        )
        self.assertFalse(user_form.is_valid())

    def test_whenUserEmailAlreadyExists_expectRaiseValidationError(self):
        ApartUser.objects.create(email='radka@abv.bg', password='parolata123')

        other_user_form = RegisterForm(
            {'email': 'radka@abv.bg',
             'password1': 'parolata321',
             'password2': 'parolata321'}
        )
        self.assertFalse(other_user_form.is_valid())

    def test_whenRegisterUser_withValidEmailAndPasswords(self):
        user_form = RegisterForm(
            {'email': 'radka@abv.bg',
             'password1': 'parolata123',
             'password2': 'parolata123'}
        )
        self.assertTrue(user_form.is_valid())
        user_form.save()
        registered_user = ApartUser.objects.get(email='radka@abv.bg')
        self.assertIsNotNone(registered_user)
