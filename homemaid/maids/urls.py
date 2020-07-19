from django.contrib import admin
from django.urls import path
from .views import MaidListView, maid_another_list_view , MaidAdd

urlpatterns = [
    path('', MaidListView.as_view(), name='maid_list'),
    path('v2/', maid_another_list_view, name='maid-another-list'),
    path('add/', MaidAdd.as_view(), name="maid_add")
]
