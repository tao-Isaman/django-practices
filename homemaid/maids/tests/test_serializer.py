from datetime import date

from django.test import TestCase
from ..serializers import MaidSerializer

from ..models import Maid


class TestMaidSerializer(TestCase):
    def test_serializer_should_object_to_json(self):
        # Given
        Maid.objects.create(
            name="BB",
            birtdate=date(1998, 4, 29),
            description="Super mad of the Year",
            certificate="Best Maid 2020",
            salary=3000
        )
        Maid.objects.create(
            name="CC",
            birtdate=date(1998, 9, 30),
            description="Ultra maid of the Year",
            certificate="Best Maid 2022",
            salary=3200
        )

        # When
        maids = Maid.objects.all()
        serializer = MaidSerializer(maids, many=True)

        # Then
        assert serializer.data == [
            {'id': 1, 'name': 'BB'},
            {'id': 2, 'name': 'CC'},
        ]
