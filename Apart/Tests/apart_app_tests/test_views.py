from django.test import TestCase, Client

from Apart.accounts.models import ApartUser


class TestViewsEstateApp(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_whenHomePageLoadsSuccessfully(self):
        response = self.test_client.get('')
        self.assertTemplateNotUsed(response, 'testing/home_page.html')

    def test_createApartmentIsPossible_WhenUserloggedIn(self):
        ApartUser.objects.create_user(email='test@abv.bg', password='parolata12345')
        self.test_client.login(email='test@abv.bg', password='parolata12345')
        response = self.test_client.get('/create/')
        self.assertEqual(response.status_code, 200)

    def test_createApartmentIsNotPossible_WhenUserNotloggedIn(self):
        response = self.test_client.get('/create/')
        self.assertEqual(response.status_code, 302)
        url = response['location']
        self.assertIn('accounts/login/', url)



