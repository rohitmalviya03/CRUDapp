from django.shortcuts import render,HttpResponseRedirect
from enroll import views
from django.shortcuts import render,redirect,HttpResponse
from .forms import StudentRegistration
from .models import User

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pwd)
            reg.save()
        fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/dashboard.html',{'form':fm,'stu':stud})

def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request,'enroll/update.html',{'form':fm})

def delete_Data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
def login(request):
    if request.method =='GET':
        return render(request,'enroll/login.html')
    else:
        email = request.POST.get('email')
        password =request.POST.get('password')
        print(email)
           



def user_profile(request):
    return render(request,'enroll/profile.html')
