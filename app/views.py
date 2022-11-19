from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes
from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.
import json




def index(request):
    return render(request, 'index.html')

def home(request, model):
    context = {}

    if request.method == 'GET':

        return render(request, 'home.html', context)

def retrain(request):
    if request.method == 'POST':
        params = json.loads(request.body)

        return HttpResponse(status=200)
    return HttpResponse(status=400)
