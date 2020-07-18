from django.test import TestCase
from django.urls import reverse


class TestListView(TestCase):
    def test_view_should_response_200(self):
        response = self.client.get(reverse('maid_list'))
        assert response.status_code == 200
