from django.contrib import admin

# Register your models here.
from .models import Student, Vehicle

admin.site.register(Student)
admin.site.register(Vehicle)