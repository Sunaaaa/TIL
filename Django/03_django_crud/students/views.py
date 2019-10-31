from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()
    content = {
        'students' : students
    }

    return render(request, 'students/index.html', content)

def new(request):
    return render(request, 'students/new.html')

def create(request):
    
    name = request.POST.get('name')
    age = request.POST.get('age')
    student = Student(name=name, age=age)
    student.save()

    return redirect('students:index')


def detail(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    content = {
        'student' : student
    }

    return render(request, 'students/detail.html', content)

def edit(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    content = {
        'student' : student
    }
    return render(request, 'students/edit.html', content)

def update(request, student_pk):

    student = Student.objects.get(pk=student_pk)
    student.name = request.POST.get('name')
    student.age = request.POST.get('age')
    student.save()

    return redirect('students:detail', student_pk)
    

def delete(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    student.delete()

    return redirect('students:index')