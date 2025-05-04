from django.urls import path

from .views import base , add_student , students

urlpatterns = [
    path('' , base , name='base'),
    path('students/' , students , name='students'),
    path('add_student/' , add_student , name='add_student'),
]