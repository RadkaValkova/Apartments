from Apart.inquiry.models import Inquiry
from Tests.base.tests import ApartTestCase


class InquiryModelTests(ApartTestCase):

    # there is not custom validators in the model. test only success
    def test_whenInquiryModel_ExpectSuccess(self):
        inquiry = Inquiry(
            first_name='Radka',
            last_name='Valkova',
            town='Plovdiv',
            email='radka@abv.bg',
            phone='888888',
            category=self.create_category_instance(),
            date='2021-07-30',
            text='text'
        )

        inquiry.full_clean()
        inquiry.save()
