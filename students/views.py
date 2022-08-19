from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Student
from .forms import StudentForm

# Create your views here.
def index(request):
    return render(request,'students/index.html',{
        'students': Student.objects.all() #Student=class name in models.py
    })
def view_student(request,id):
    student=Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        #creating a form instance and populate it with data from the request
        form =StudentForm(request.POST)
        #checking whether the form is valid .If it is valid then process the data in form.cleaned_data.We can use that data to upload in db or for other processing
        if form.is_valid():
            new_student_number=form.cleaned_data['student_number']
            new_first_name=form.cleaned_data['first_name']
            new_last_name=form.cleaned_data['last_name']
            new_email=form.cleaned_data['email']
            new_field_of_study=form.cleaned_data['field_of_study']
            new_gpa=form.cleaned_data['gpa']

            new_student = Student(
                student_number=new_student_number,
                first_name=new_first_name,
                last_name=new_last_name,
                email=new_email,
                field_of_study=new_field_of_study,
                gpa=new_gpa,
            )
            new_student.save()
            return render(request,'students/add.html',{
                #these are variables
                'form':StudentForm(),
                'success':True
            })
       
    else:
        # creating form instance for blank form
        form=StudentForm()
        return render(request,'students/add.html',{
            'form':StudentForm() #can use {{ form }} which is equal to blank form(unbound form)
        })

def edit(request,id):
    if request.method == 'POST':
        #student details whose pk(in the db)=id passed as an argument through url(<int:id>)
        student = Student.objects.get(pk=id)
        #instantiate student form with request.post argument
        #2nd arg->to ensure that we added info of the crct student
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return render(request,'students/edit.html',{
                'form':form,
                'success':True
            })
    # if the request is not post then we only show form but we dont update it(but i gave method=post in form in edit.html)
    else:
        #we dont return response here
        student = Student.objects.get(pk=id)
        #instantiate student form
        #arg->to ensure that we added info of the crct student
        form = StudentForm(instance=student)
    return render(request,'students/edit.html',{
        'form':form
    })

def delete(request,id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        # delete method is used to delete student record
        student.delete()
    return HttpResponseRedirect(reverse('index'))
