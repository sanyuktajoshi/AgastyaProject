from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .forms import UserForm
from django.db.models import DateTimeField
from .models import User, Student, Contributor
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def user_login(request):
    isContrib=False
    if request.method == "POST":
        if "login" in request.POST:
            print("Entered Login")
            email = request.POST.get('email')
            password = request.POST.get('password')
            UserModel = get_user_model()
            try:
                user = UserModel.objects.get(email=email)
            except UserModel.DoesNotExist:
                return render(request, 'login.html')
            else:
                if user.check_password(password):
                    login(request,user)
                    
                    if Student.objects.filter(user=user).exists():
                        return render(request,'home.html')
                    else:
                        isContrib=True
                        return render(request,'home.html',{"isContrib":isContrib})
                            
        if "mentorsignup" in request.POST:
            print("Entered Contributor Signup")
            # Save in users
            fullname = request.POST.get('fullname')
            # username = request.POST.get('contrib')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user_form=UserForm(data={'username': fullname,"email":email,"password":password})
            if user_form.is_valid():
                userc=user_form.save()
                userc.set_password(password)
                userc.save()
            # Save in Univ table also
            obj= User.objects.get(username=fullname)
            adduniv= Contributor(user=obj)
            adduniv.save()

        if "studentsignup" in request.POST:
            print("Entered Student Signup")
            fullname = request.POST.get('fullname')
            school= request.POST.get('school')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user_form=UserForm(data={'username': fullname,'school':school,"email":email,"password":password})
            if user_form.is_valid():
                userc=user_form.save()
                userc.set_password(password)
                userc.save()
            
            # Save in student table also
            obj= User.objects.get(username=fullname)
            # obj2= University.objects.get(name=university)
            addstudent= Student(user=obj,school=school)
            addstudent.save()
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return render(request,'home.html',{"isUniv":False})
