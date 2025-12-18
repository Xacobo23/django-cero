from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. #Evidentemente el nombre variara entre cada proyecto, pero esta es la idea principal.
def home(request):
    return render(request, 'PasswordApp/home.html')

def getPassword(request):
    return render(request, 'PasswordApp/getPassword.html')

def about(request):
    return render(request, 'PasswordApp/about.html')