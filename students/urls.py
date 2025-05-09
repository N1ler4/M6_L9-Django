from django.urls import path
from .views import base, add_student, students, signup, signin, logout, change_password, Auth1

urlpatterns = [
    path('', base, name='base'),
    path('students/', students, name='students'),
    path('add_student/', add_student, name='add_student'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', logout, name='logout'),
    path('change_password/', change_password, name='change_password'),
    path('send-email/', Auth1.as_view(), name='send_email'),
]
