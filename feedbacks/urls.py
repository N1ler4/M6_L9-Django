from django.urls import path
from .views import feedbacks, add_feedback , feedback_detail

urlpatterns = [
    path('feedbacks/', feedbacks, name='feedbacks'),
    path('add_feedback/', add_feedback, name='add_feedback'),
    path('feedbacks/<int:pk>/', feedback_detail, name='feedback_detail')

]