from django.test import TestCase

from Apart.inquiry.models import Inquiry


class InquiryModelTests(TestCase):
    valid_first_name = 'Radka'
    valid_last_name = 'Valkova'
    valid_town = 'Plovdiv'
    valid_email = 'radka@abv.bg'
    valid_phone = '888 888'
    valid_category = 'друго'
    valid_date = '2021-07-30'
    valid_tex = 'text'

    # there is not custom validators in the model. test only success
    def test_whenInquiryModel_ExpectSuccess(self):
        inquiry = Inquiry(
            first_name=self.valid_first_name,
            last_name=self.valid_last_name,
            town=self.valid_town,
            email=self.valid_email,
            phone=self.valid_phone,
            category=self.valid_category,
            date=self.valid_date,
            text=self.valid_tex
        )

        inquiry.full_clean()
        inquiry.save()
