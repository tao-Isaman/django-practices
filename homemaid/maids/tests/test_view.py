from datetime import date
from unittest.mock import patch
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


class testMaidView(TestCase):
    def test_view_should_response_200(self):
        response = self.client.get(reverse('maid_add'))
        assert response.status_code == 200

    def test_view_should_have_maid_form(self):
        response = self.client.get(reverse('maid_add'))
        print(response.content)
        assert '<input type="hidden" name="csrfmiddlewaretoken"' in str(
            response.content)

        assert '<form action="." method="POST">' in str(response.content)

        name_field = 'input type="text" name="name" maxlength="300" required id="id_name"'
        assert name_field in str(response.content)

        button = '<button type="submit" class="btn btn-primary">Add maids</button>'
        assert button in str(response.content)

    def test_summit_from_should_save_new_maid(self):
        data = {
            'name': 'BB'
        }
        self.client.post(reverse('maid_add'), data=data)
        maid = Maid.objects.last()
        assert maid.name == 'BB'

    @patch('maids.views.send_mail')
    def test_after_submit_form_email_should_be_sent(self, mock):
        data = {
            'name': "BB"
        }
        self.client.post(reverse('maid_add'), data=data)

        mock.assert_called_once_with('Subject here', 'Here is the message.',
                                     'from@example.com', ['to@example.com'], fail_silently=False)
