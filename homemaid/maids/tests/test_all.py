from datetime import date
from unittest.mock import MagicMock

from django.test import TestCase
from django.core.files import File


from ..models import Maid


# Create your tests here.
class TestMaid(TestCase):
    def test_model_should_have_name_defined_fields(self):
        # Given
        Maid.objects.create(
            name="BB",
            birtdate=date(1998, 4, 29),
            description="Super mad of the Year",
            certificate="Best Maid 2020",
            salary=3000
        )
        # When
        maid = Maid.objects.last()
        # Then
        assert maid.name == "BB"
        assert maid.birtdate == date(1998, 4, 29)
        assert maid.description == "Super mad of the Year"
        assert maid.certificate == "Best Maid 2020"
        assert maid.salary == 3000

    def test_model_should_have_image_defined_fields(self):
        # Given
        mock = MagicMock(spec=File)
        mock.name = "profile.png"
        Maid.objects.create(
            name="BB",
            profile_image=mock.name,
            birtdate=date(1998, 4, 29),
            description="Super mad of the Year",
            certificate="Best Maid 2020",
            salary=3000
        )
        # When
        maid = Maid.objects.last()
        # Then
        assert maid.profile_image.name == 'profile.png'

    def test_model_should_have_created_and_modified_fields(self):
        # Given
        mock = MagicMock(spec=File)
        mock.name = "profile.png"
        Maid.objects.create(
            name="BB",
            profile_image=mock.name,
            birtdate=date(1998, 4, 29),
            description="Super mad of the Year",
            certificate="Best Maid 2020",
            salary=3000
        )
        # When
        maid = Maid.objects.last()

        # Then
        assert maid.created is not None
        assert maid.modified is not None
