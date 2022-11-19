from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
from .models import Student, Vehicle
import json



def index(request):
    context = {
        'ClassA': [],
        'ClassB': [],
    }
    students = Student.objects.all()
    for student in students:
        if student.status == 0: # should be 1
            data = str(student)
            if student.classes == 0:
                context['ClassA'].append(data)
            else:
                context['ClassB'].append(data)

    return render(request, 'index.html', context)

def home(request, model):
    context = {}
