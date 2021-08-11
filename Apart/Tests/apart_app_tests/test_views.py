from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.urls import reverse

from Tests.base.tests import ApartTestCase


class HomePageTests(ApartTestCase):

    def test_whenHomePageLoadsSuccessfully(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'testing/home_page.html')

    def test_getAllAparts_shouldRenderTemplate(self):
        response = self.client.get(reverse('all aparts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'aparts/all_aparts.html')


class CreateApartmentsTests(ApartTestCase):

    def test_createApartmentIsPossible_WhenUserLoggedIn(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)

    def test_createApartmentIsNotPossible_WhenUserNotLoggedIn(self):
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 302)

    def test_getApartmentCreateForm_shouldRenderTemplate_IfLogin(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('create'))
        self.assertTemplateUsed(response, 'aparts/create.html')

    def test_createApartment(self):
        self.client.force_login(self.user)
        apart = self.create_apart(
            type=self.create_type_instance(),
            town='Пловдив',
            construction=self.create_construction_instance(),
            construction_year='2021',
            deal=self.create_deal_instance(),
            status=self.create_status_instance(),
            price_offer=20000,
            price_realized=0,
            pure_area=50,
            total_area=50,
            finishing_works=self.create_fifnishing_works_instance(),
            furnishing=self.create_furnishing_instance(),
            description='описание',
            image='image.jpg',
            date='2021-07-30',
            email='radka@abv.bg',
            contact_phone='88888',
            user=self.user,
        )
        response = self.client.get(reverse('all aparts', ))
        self.assertEqual(len(response.context['aparts']), 1)


class ApartmentDetailsTests(ApartTestCase):

    def test_getApartDetails_whenApartExistsAndIsSelfUser_shouldReturnDetailsForSelfUser(self):
        self.client.force_login(self.user)
        apart = self.create_apart(
            type=self.create_type_instance(),
            town='Пловдив',
            construction=self.create_construction_instance(),
            construction_year='2021',
            deal=self.create_deal_instance(),
            status=self.create_status_instance(),
            price_offer=20000,
            price_realized=0,
            pure_area=50,
            total_area=50,
            finishing_works=self.create_fifnishing_works_instance(),
            furnishing=self.create_furnishing_instance(),
            description='описание',
            image='image.jpg',
            date='2021-07-30',
            email='radka@abv.bg',
            contact_phone='88888',
            user=self.user,
        )
        response = self.client.get(reverse('apart details', kwargs={'pk': apart.id}))
        self.assertTrue(response.context['is_user'])

    def test_getApartDetails_whenApartExistsAndIsOtherUser_shouldReturnDetailsForOtherUser(self):
        self.client.force_login(self.user)
        other_user = self.create_user(email='other@abv.bg', password='parolata123')
        apart = self.create_apart(
            type=self.create_type_instance(),
            town='Пловдив',
            construction=self.create_construction_instance(),
            construction_year='2021',
            deal=self.create_deal_instance(),
            status=self.create_status_instance(),
            price_offer=20000,
            price_realized=0,
            pure_area=50,
            total_area=50,
            finishing_works=self.create_fifnishing_works_instance(),
            furnishing=self.create_furnishing_instance(),
            description='описание',
            image='image.jpg',
            date='2021-07-30',
            email='radka@abv.bg',
            contact_phone='88888',
            user=other_user,
        )
        response = self.client.get(reverse('apart details', kwargs={'pk': apart.id}))
        self.assertFalse(response.context['is_user'])


class EditApartmentTests(ApartTestCase):
    im = Image.new(mode='RGB', size=(200, 200))
    im_io = BytesIO()
    im.save(im_io, 'JPEG')
    im_io.seek(0)
    image = InMemoryUploadedFile(im_io, None, 'random-name.jpg', 'image/jpeg', len(im_io.getvalue()), None)

    def test_editPossible_whenUserIsApartmentOwner(self):
        self.client.force_login(self.user)
        apart = self.create_apart(
            type=self.create_type_instance(),
            town='Пловдив',
            construction=self.create_construction_instance(),
            construction_year='2021',
            deal=self.create_deal_instance(),
            status=self.create_status_instance(),
            price_offer=20000,
            price_realized=0,
            pure_area=50,
            total_area=50,
            finishing_works=self.create_fifnishing_works_instance(),
            furnishing=self.create_furnishing_instance(),
            description='описание',
            image=self.image,
            date='2021-07-30',
            email='radka@abv.bg',
            contact_phone='88888',
            user=self.user,
        )

        edit_url = reverse('edit', args=(apart.pk,))
        response = self.client.get(edit_url)
        form = response.context['form']
        data = form.initial
        data['image'] = self.image
        data['town'] = 'Varna'
        response = self.client.post(edit_url, data)
        self.assertContains(response, 'Varna')


# class DeleteApartmentTests(ApartTestCase):
#
#     def test_DeletePossible_whenUserIsApartmentOwner(self):
#         self.client.force_login(self.user)
#         apart = self.create_apart(
#             type=self.create_type_instance(),
#             town='Пловдив',
#             construction=self.create_construction_instance(),
#             construction_year='2021',
#             deal=self.create_deal_instance(),
#             status=self.create_status_instance(),
#             price_offer=20000,
#             price_realized=0,
#             pure_area=50,
#             total_area=50,
#             finishing_works=self.create_fifnishing_works_instance(),
#             furnishing=self.create_furnishing_instance(),
#             description='описание',
#             image='image.jpg',
#             date='2021-07-30',
#             email='radka@abv.bg',
#             contact_phone='88888',
#             user=self.user,
#         )
#
#         delete_url = reverse('delete', args=(apart.pk,))
#         response = self.client.post(delete_url)
#
#         self.assertEqual(response.status_code, 302)













