from django.db import models

# Create your models here.


class Teacher(models.Model):
    SUBJECT_CHOICES = [
        ('Math', 'Math'),
        ('Science', 'Science'),
        ('English', 'English'),
        ('History', 'History'),
        ('Geography', 'Geography'),
    ]

    full_name = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
