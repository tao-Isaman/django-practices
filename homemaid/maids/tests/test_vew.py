from django.test import TestCase

class TestListView(TestCase):
    def test_view_should_response_200(self):
        response = self.client.get('/maids/')
        assert response.status_code == 200