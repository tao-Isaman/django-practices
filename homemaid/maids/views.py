from django.shortcuts import render
from django.http import HttpResponse, request
from django.views import View

from .models import Maid

# Create your views here.


class MaidListView(View):
    template_name = 'maidlist.html'

    def get(self, request):
        context = {
            'maid_list': Maid.objects.all()
        }
        return render(request, self.template_name, context)


def maid_another_list_view(request):
    html = ""
    for m in Maid.objects.all():
        html += f'<li>{m.name}</li>'
    return HttpResponse(html)
