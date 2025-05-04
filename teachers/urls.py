from django.urls import path
from .views import add_teacher, teachers

urlpatterns = [
    path('teachers/', teachers, name='teachers'),
    path('add_teacher/', add_teacher, name='add_teacher'),
]
