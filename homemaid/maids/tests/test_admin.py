from django.contrib import admin
from django.test import TestCase

from ..admin import MaidAdmin
from ..models import Maid


class TestMaidAdmin(TestCase):
    def test_admin_shold_be_register(self):
        assert isinstance(admin.site._registry[Maid], MaidAdmin)

    def test_admin_should_set_list_display(self):
        excepted = (
            'name',
            'birtdate',
            'description',
            'certificate',
            'salary'
        )
        assert MaidAdmin.list_display == excepted
