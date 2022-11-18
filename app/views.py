from django.shortcuts import render
from django.http import HttpResponse

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
