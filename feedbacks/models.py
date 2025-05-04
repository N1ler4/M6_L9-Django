from django.db import models

# Create your models here.

class Feedback(models.Model):
    student_name = models.CharField(max_length=100)
    feedback_text = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.student_name} on {self.date_submitted.strftime('%Y-%m-%d')}"