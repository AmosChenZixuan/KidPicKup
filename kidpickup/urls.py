from django.urls import include, path
from django.contrib import admin
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signUp/<str:carid>/', views.signUp, name='signUp'),
    path('signOut/<str:studentid>/', views.signOut, name='markAsLeft'),
    path('cars/', views.getAllCars, name='getAllCars'),
    path('reset/', views.reset, name='backdoor-reset')
]

