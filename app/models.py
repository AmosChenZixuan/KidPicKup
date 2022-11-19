from django.db import models
from django.core.validators import MinLengthValidator


class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name  = models.CharField(max_length=32)
    status     = models.PositiveSmallIntegerField()
    classes    = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Vehicle(models.Model):
    student_id      = models.ForeignKey(Student, on_delete=models.CASCADE)
    registration_id = models.CharField(max_length=6, validators=[MinLengthValidator(6)])

    def __str__(self):
        return self.registration_id

class WaitingList(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)