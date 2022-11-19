from django.contrib import admin

# Register your models here.
from .models import Student, Vehicle, WaitingList

admin.site.register(Student)
admin.site.register(Vehicle)
admin.site.register(WaitingList)