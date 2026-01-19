from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        labels = {
            "name" : "Enter your name",
            "degree" : "Enter your degree"
        }

        error_messages = {
            "name" : {
                "required" : "This field can not be empty",
                "max_length": "Your name may be shorter"
            }
        }