from django.test import TestCase
from ..form import MaidForm


class TestMaidFrom(TestCase):
    def test_from_should_have_defined_fields(self):

        form = MaidForm()
        assert len(form.fields) == 1
        assert 'name' in form.fields
