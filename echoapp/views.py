from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.

class index(View):
    def get(self, request):
        return HttpResponse("public_html")


class img(View):
    def get(self, request):
        return render_to_response('index.html')
