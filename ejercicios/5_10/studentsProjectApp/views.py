from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student 
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormView

from django.views.generic import CreateView

# Create your views here. #Evidentemente el nombre variara entre cada proyecto, pero esta es la idea principal.
def home(request):
    students = Student.objects.all()
    return render(request, 'studentsProjectApp/home.html', {"students":students})

# def student(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/home.html")
#     else:
#         form = StudentForm()
    
#     return render(request, "studentsProjectApp/studentForm.html", {"form": form})

class StudentList(ListView):
    template_name = "studentsProjectApp/studentList.html"
    model = Student
    context_object_name = "students"

class StudentDetail(DetailView):
    template_name = "studentsProjectApp/student.html"
    model = Student
    context_object_name = "student"


class StudentCreate(CreateView):
    model=Student
    form_class=StudentForm
    template_name= "studentsProjectApp/studentForm.html"
    success_url="/"