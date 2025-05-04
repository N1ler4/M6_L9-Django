from django.shortcuts import render , redirect
from .forms import StudentForm
from .models import Student
# Create your views here.

def base(request):
    return render(request, 'base.html')

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students') 
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

def students(request):
    students = Student.objects.all()
    return render(request, 'students/students.html', {'students': students})
