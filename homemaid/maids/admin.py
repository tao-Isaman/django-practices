from django.contrib import admin

from .models import Maid

# Register your models here.


@admin.register(Maid)
class MaidAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'birtdate',
        'description',
        'certificate',
        'salary',
    )
