from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. #Evidentemente el nombre variara entre cada proyecto, pero esta es la idea principal.
def home(request):
    return render(request, 'BlogApp/home.html')