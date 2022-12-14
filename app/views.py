from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
from .models import Student, Vehicle, WaitingList
from .consumers import notify_student_added, notify_student_removed


@api_view(['GET'])
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
            wl_item = wl.get(student_id = student.id)
            data = student.json()
            data['car'] = wl_item.vehicle_id
            context['Classes'][class_id].append(data)
            context['Stats'][class_id]['not_left'] += 1
        else: # picked up, left the school
            context['Stats'][class_id]['left'] += 1
    return render(request, 'index.html', context)

@api_view(['POST'])
def signUp(request, carid):
    if request.method == 'POST':
        # validate input format
        if len(carid) != 6 or not carid.isalnum():
            return HttpResponseBadRequest('Invalid Car Registration Number')

        cars = Vehicle.objects
        # fetch car 
        try:
            car = cars.get(registration_id=carid)
        except Vehicle.DoesNotExist:
            return HttpResponseNotFound('Car Registration Number Not Found')
        # fetch associated student
        student = car.student_id
        if student.status == 1:
            return HttpResponseBadRequest(f'Student({student}) is already added')
        elif student.status == 2:
            return HttpResponseBadRequest(f'Student({student}) is already left')
        # update student and create new waitlist item
        student.status = 1
        student.save()
        new_wl = WaitingList()
        new_wl.student_id = student 
        new_wl.vehicle_id = car
        new_wl.save()
        notify_student_added(new_wl)
        return HttpResponse(200)

@api_view(['POST'])
def signOut(request, studentid):
    if request.method == 'POST':
        student = Student.objects.get(pk=studentid)
        if student.status != 1:
            return HttpResponseBadRequest('Illegal Operation')
        student.status = 2
        student.save()
        notify_student_removed(student)
        return HttpResponse(200)

@api_view(['GET'])
def getAllCars(request):
    if request.method == 'GET':
        data = []
        cars = Vehicle.objects.all()
        for car in cars:
            data.append(f"{car} ({car.student_id})")

        return JsonResponse(data, safe=False)


def reset(request):
    import os 
    os.system('python insertData.py')
    return redirect(index)