from datetime import date
from django.test import TestCase
from .models import Maid


# Create your tests here.
class TestMaid(TestCase):
    def test_model_should_have_name_defined_fields(self):
        # Given
        Maid.objects.create(
            name="BB" ,
            birtdate=date(1998,4,29),
            description="Super mad of the Year",
            certificate="Best Maid 2020",
            salary=3000
        )

        # When
        maid = Maid.objects.last()

        #Then
        self.assertEqual(maid.name , "BB")
        self.assertEqual(maid.birtdate , date(1998,4,29))
        self.assertEqual(maid.description , "Super mad of the Year")
        self.assertEqual(maid.certificate , "Best Maid 2020")
        self.assertEqual(maid.salary , 3000)


        
