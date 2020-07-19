# from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Maid

# Create your views here.


class MaidListView(View):
    def get(self, request):
        html = ""
        for m in Maid.objects.all():
            html += f'<li>{m.name}</li>'
        return HttpResponse(html)


def maid_another_list_view(request):
    html = ""
    for m in Maid.objects.all():
        html += f'<li>{m.name}</li>'
    return HttpResponse(html)
