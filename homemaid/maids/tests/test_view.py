from datetime import date

from django.test import TestCase
from django.urls import reverse

from ..models import Maid


class TestListView(TestCase):
    def test_view_should_response_200(self):
        response = self.client.get(reverse('maid_list'))
        assert response.status_code == 200

    def test_ciew_should_display_maid_list(self):
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
        responese = self.client.get(reverse('maid_list'))
        # Then
        assert '<li>BB</li>' in str(responese.content)
        assert '<li>CC</li>' in str(responese.content)


class testMaidListAnotherView(TestCase):
    def test_view_should_display_maid_list(self):
        response = self.client.get(reverse('maid-another-list'))
        assert response.status_code == 200
    
    def test_ciew_should_display_maid_list(self):
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
        responese = self.client.get(reverse('maid-another-list'))
        # Then
        assert '<li>BB</li>' in str(responese.content)
        assert '<li>CC</li>' in str(responese.content)