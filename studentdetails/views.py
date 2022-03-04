from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def homepage(request):
    return render(request,'home.html')

def rec_data(request):
    Firstname = ""
    Lastname=""
    RollNumber=""
    Class=""

    if request.method == 'POST':
      Firstname= request.POST["fname"]
      Lastname = request.POST["lname"]
      RollNumber=request.POST["Rnum"]
      Class = request.POST["cls"]


    dicta = {
         'First_name': Firstname,'Last_name': Lastname,'Roll_number': RollNumber,'Class':Class }


    s=Student()
    s.Firstname = Firstname
    s.Lastname = Lastname
    s.RollNumber=RollNumber
    s.Class=Class
    s.save()
    all_students = Student.objects.all()
    context = dict()
    context['all_students'] = all_students
    return render(request,'rec_data.html',context=context)

def homepage(request):
    return render(request,'home.html')

def table_data(request):
    return render(request,'table_data.html')


