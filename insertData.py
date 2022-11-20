import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kidpickup.settings')
django.setup()
from app.models import Student, Vehicle, WaitingList
import random
random.seed(10)


LAST_NAME = ['Alice', 'Bob', 'Chris', 'David', 'Ellis', 'Frank', 'Grey', "Hart", 'Ivy', "Jean", "Kevin"]
FIRST_NAME = ['Logan', 'Mark', 'Nicholas', 'Oliver', 'Peter', 'Quinn', 'Ruby', 'Sun', 'Tyler']
ALNUM = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789012345678901234567890'

N_A, N_B = 10, 15

def generate_name():
    return random.choice(FIRST_NAME), random.choice(LAST_NAME)

def generate_reg_num(classes):
    ret = classes
    for _ in range(5):
        ret += random.choice(ALNUM)
    return ret

def new_student(cid):
    student = Student()
    fname, lname = generate_name()
    student.first_name = fname 
    student.last_name  = lname
    student.classes    = cid
    student.status     = 0
    student.save()
    return student

def new_car(student, classes):
    car = Vehicle() 
    car.student_id = student
    registration = generate_reg_num(classes)
    car.registration_id = registration
    car.save()
    return car

def generate_data(n, classes, cid, file):
    file.write(f"===={classes}====\n")
    for i in range(n):
        student = new_student(cid)
        cars = []
        # at least one car associated to a student
        cars.append(new_car(student, classes))
        while random.random() < .1:
            cars.append(new_car(student, classes))

        file.write(f"{student}:{' '.join(car.registration_id for car in cars)}\n")

if __name__ == '__main__':
    # drop existing
    Student.objects.all().delete()
    Vehicle.objects.all().delete()
    WaitingList.objects.all().delete()

    with open('data.txt', 'w') as file:
        generate_data(N_A, 'A', 0, file)
        generate_data(N_B, 'B', 1, file)
    
