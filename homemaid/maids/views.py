from django.shortcuts import render
from django.http import HttpResponse, request
from django.views import View
from django.core.mail import send_mail

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Maid
from .form import MaidForm
from .serializers import MaidSerializer

# Create your views here.


class MaidListView(View):
    template_name = 'maidlist.html'

    def get(self, request):
        context = {
            'maid_list': Maid.objects.all()
        }
        return render(request, self.template_name, context)


class MaidAdd(View):
    template_name = 'maid_add.html'

    def get(self, request):
        form = MaidForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = MaidForm(request.POST)
        if form.is_valid():
            form.save()
        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )

        return HttpResponse()


class MaidListAPIView(APIView):
    def get(self, request):
        maids = Maid.objects.all()
        serializer = MaidSerializer(maids, many=True)
        return Response(serializer.data)


def maid_another_list_view(request):
    template_name = 'maidlist.html'
    context = {
        'maid_list': Maid.objects.all()
    }
    return render(request, template_name, context)
