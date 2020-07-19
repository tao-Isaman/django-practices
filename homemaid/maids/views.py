from django.shortcuts import render
from django.http import HttpResponse, request
from django.views import View

from .models import Maid

# Create your views here.


class MaidListView(View):
    def get(self, request):
        #     html = ""
        #     for m in Maid.objects.all():
        #         html += f'<li>{m.name}</li>'
        #     return HttpResponse(html)

        # ===================================================

        maid_list = []
        for m in Maid.objects.all():
            maid_list.append(m.name)
        template = 'maidlist.html'
        context = {
            'maid_list': maid_list
        }
        return render(request, template, context)


def maid_another_list_view(request):
    html = ""
    for m in Maid.objects.all():
        html += f'<li>{m.name}</li>'
    return HttpResponse(html)
