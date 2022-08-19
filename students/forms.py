from dataclasses import fields
from socket import fromshare
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student #fields taking from which model(Student model)
        fields=['student_number','first_name','last_name','email','field_of_study','gpa'] # or fields="__all__"
        # labels of a form for various fields 
        labels={
            'student_number': 'Student Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'field_of_study':'Field of study',
            'gpa':'GPA',
        }
        # to style form we use bootstrap class form-control.Styling is done with the help of widgets in django
        widgets={
            'student_number':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'field_of_study':forms.TextInput(attrs={'class':'form-control'}),
            'gpa':forms.NumberInput(attrs={'class':'form-control'}),
        }