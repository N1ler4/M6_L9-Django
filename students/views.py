from django.shortcuts import render, redirect
from .forms import StudentForm, SignUpForm 
from .models import Student
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login
from django.contrib.auth import update_session_auth_hash
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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, 'auth/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('/')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            return redirect('/')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'auth/change_password.html', {'form': form})