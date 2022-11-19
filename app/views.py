from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.http import JsonResponse


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


def signUp(request, carid):
    if request.method == 'POST':
        if len(carid) != 6 or not carid.isalnum():
            return HttpResponseBadRequest('Invalid Car Registration Number')

        cars = Vehicle.objects
        students = Student.objects
        
        try:
            car = cars.get(registration_id=carid)
        except Vehicle.DoesNotExist:
            return HttpResponseNotFound('Car Registration Number Not Found')
        student = students.get(pk=car.student_id.id)
        if student.status == 1:
            return HttpResponseBadRequest(f'Student({student}) Already Added')
        elif student.status == 2:
            return HttpResponseBadRequest(f'Student({student}) Already Left')
        student.status = 1
        student.save()
        new_wl = WaitingList()
        new_wl.student_id = student 
        new_wl.vehicle_id = car
        new_wl.save()
        
        return HttpResponse(200)
