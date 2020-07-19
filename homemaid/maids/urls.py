from django.contrib import admin
from django.urls import path
from .views import MaidListView, maid_another_list_view

urlpatterns = [
    path('', MaidListView.as_view(), name='maid_list'),
    path('/list', maid_another_list_view, name='maid-another-list')
]
