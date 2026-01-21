from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from .forms import StudentForm
from .models import Student 
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormView

from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


# Create your views here. #Evidentemente el nombre variara entre cada proyecto, pero esta es la idea principal.
def home(request):
    students = Student.objects.all()
    return render(request, 'studentsProjectApp/home.html', {"students":students})

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
    success_url=reverse_lazy('studentList')

class StudentUpdate(UpdateView):
    model=Student
    form_class=StudentForm
    template_name="studentsProjectApp/studentUpdate.html"

    def get_success_url(self):
        return reverse('studentDetail', kwargs={'pk': self.object.pk})

class StudentDelete(DeleteView):
    model=Student
    template_name="studentsProjectApp/studentConfirmDelete.html"
    success_url= reverse_lazy('studentList')