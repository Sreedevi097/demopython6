from django.contrib import messages, auth
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from .form import  TaskForm1
from taskapp.models import task
from taskapp.models import task1

def school(request):
    return render(request, "school.html")
def newpage(request):
    return render(request, "newpage.html")
def Form(request):
    tasks1 = task1.objects.all()
    if request.method == "POST":
        name = request.POST.get('Name:-', )
        dob = request.POST.get('DOB:-', )
        tasks1 = task1(name=name, dob=dob)
        tasks1.save()
        return redirect('form/')
        messages.info(request, "email taken")
    return render(request, 'Form.html')
def login(request):
    task1 = task.objects.all()
    if request.method == "POST":
        username = request.POST.get('username', )
        password = request.POST.get('password', )
        if username==username:
            return redirect('newpage/')
    return render(request, "login.html")

def register(request):
        tasks = task.objects.all()
        if request.method == "POST":
            username = request.POST.get('username', )
            password = request.POST.get('password', )
            tasks = task(username=username, password=password)
            tasks.save()
            return redirect('login/')
        return render(request, 'Register.html')

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST.get('password')
#         user = auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('/')
#         else:
#             messages.info(request, "invalid credentials")
#             return redirect('/')
#     return render(request, "login.html")
# def Register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST.get('password')
#         cpassword = request.POST['cpassword']
#         if password==cpassword:
#                 user = User.objects.create_user(username=username,password=password)
#                 user.save()
#                 print("user created")
#                 return redirect('login')
#         else:
#             messages.info(request,"password not matching")
#             return redirect('/')
#     return render(request,"Register.html")

