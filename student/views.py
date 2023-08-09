from django.shortcuts import render,redirect
from .forms import StudentRegistration
from.models import Student
from django.contrib import messages
# Create your views here.

def home(request):
    if 'id' in request.GET:
        id = request.GET['id']
        data = Student.objects.filter(id=id)
    else:
        data = Student.objects.all().order_by('id')
    return render(request,'home.html',{'data':data})

def addStudent(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,message="You Add a student successfully")
            return redirect('home')
    else:
        form = form = StudentRegistration()
    return render(request,'add.html',{'form':form})

def delete_student(request,id):
    Student.objects.filter(id=id).delete()
    return redirect('home')

def update_info(request,id):
    student = Student.objects.get(id = id)
    form = StudentRegistration(instance=student)
    if request.method =='POST':
        form = StudentRegistration(request.POST,instance=student)
        if form.is_valid():
            messages.success(request,message="You successfully update your data")
            form.save()
            return redirect('home')
    return render(request,'update_form.html',{'form':form})
