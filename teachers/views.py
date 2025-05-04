from django.shortcuts import redirect, render
from .forms import TeacherForm
from .models import Teacher

# Create your views here.

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students') 
    else:
        form = TeacherForm()
    return render(request, 'teachers/add_teacher.html', {'form': form})


def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teachers.html', {'teachers': teachers})
