import random
from django.shortcuts import render, redirect
from .forms import StudentForm, SignUpForm 
from .models import Student
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator
from .email import send_to_mail
from django.views.generic import View
import string
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
    students_list = Student.objects.all()
    paginator = Paginator(students_list, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'students/students.html', {
        'students': page_obj,
        'page_obj': page_obj
    })


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

import random
import string
from django.views import View
from django.shortcuts import render
from django.core.mail import send_mail

class Auth1(View):
    def get(self, request):
        return render(request, 'auth/send_mail.html')

    def post(self, request):
        email = request.POST.get('email')
        int_ = string.digits
        str_ = string.ascii_letters
        code = ''.join(random.choice(int_ + str_) for _ in range(6))

        print(f"Сгенерированный код: {code}")

        send_mail(
            subject='Ваш код подтверждения',
            message=f'Ваш код: {code}',
            from_email='your_email@gmail.com',
            recipient_list=[email],
            fail_silently=False,
        )

        return render(request, 'auth/send_mail.html', {'code': code})
