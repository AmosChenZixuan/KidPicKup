from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
from .models import Student, Vehicle, WaitingList
import json



def index(request):
    context = {
        'Classes': [[] for _ in range(2)],
        'Stats':  [{'left':     0,
                    'not_left': 0} for _ in range(2)],
    }
    students = Student.objects.all()
    wl = WaitingList.objects

    for student in students:
        class_id = student.classes
        if student.status == 0: # still in school and not been called
            context['Stats'][class_id]['not_left'] += 1
        
        elif student.status == 1: # waiting to be picked up
            student_name = str(student)
            wl_item = wl.get(student_id = student.id)
            data = f"{student_name} ({wl_item.vehicle_id})"
            context['Classes'][class_id].append(data)
            context['Stats'][class_id]['not_left'] += 1
        else: # picked up, left the school
            context['Stats'][class_id]['left'] += 1
    return render(request, 'index.html', context)

def home(request, model):
    context = {}
