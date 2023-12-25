from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .forms import UserForm
from django.db.models import DateTimeField
from .models import User, Student, Contributor, Project
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404, redirect
from .models import Project, Contributor
from django.contrib import messages

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

def upload_project(request):
    if request.method=='POST':
        projectName = request.POST['projectName']
        overview = request.POST['overview']
        project_image=request.POST['image']
        links = request.POST['links']
        funds=request.POST['fundsNeeded']
        current_student = Student.objects.get(user=request.user)
        project_obj = Project(name=projectName, overview=overview, necessary_links=links, images=project_image, funds_needed=funds, student=current_student )
        project_obj.save()
        # return render(request, 'uploadForm.html', {'domain_tags': domain_tags, 'universities': universities, 'student_list': student_emails, 'current_user_uni': current_user_uni})
        return redirect('home')
    else:
        return render(request, 'uploadForm.html')
    
def explore(request):
    projects = Project.objects.all
    return render(request, 'exploreProjects.html', {'projects': projects})

def projectDetails(request, pk):
    project=Project.objects.get(pk=pk)
    isContrib=False
    if request.user.is_authenticated:
        if hasattr(request.user, 'contributor'):
            isContrib=True
    return render(request, 'projectDetails.html', {'project' : project,'isContrib':isContrib})

def become_mentor(request, pk):
    project = get_object_or_404(Project, pk=pk)
    contributor = Contributor.objects.get(user=request.user)

    # Set the is_mentor field to True for the contributor
    contributor.is_mentor = True
    contributor.save()
    messages.success(request, 'You are now a mentor!')
    # Add the contributor to the mentors of the project
    project.mentors.add(contributor)
    project.save()

    return redirect('projectDetails', pk=pk)  # Redirect to the project details page

def become_sponsor(request, pk):
    project = get_object_or_404(Project, pk=pk)
    contributor = Contributor.objects.get(user=request.user)

    # Set the is_sponsor field to True for the contributor
    contributor.is_sponsor = True
    isSponsor=contributor.is_sponsor
    contributor.save()
    
    messages.success(request, 'You are now a sponsor!')
    # Add the contributor to the sponsors of the project
    project.sponsors.add(contributor)
    project.save()

    return redirect('projectDetails', pk=pk)  # Redirect to the project details page
