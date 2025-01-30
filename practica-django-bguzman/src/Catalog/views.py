
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required

from Catalog import models
from Catalog.form import CourseForm, TeacherForm

# Create your views here.

def courses(request):
    courses = models.Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def teachers(request):
    teachers = models.Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

@login_required
def index(request):
    if request.session.get('counter') == None:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1
    return render(request, 'index.html' , {'counter': request.session['counter']})

def create_course(request):
    if request.method == 'POST':
        course = models.Course()
        course.name = request.POST.get('name')
        course.description = request.POST.get('description')
        course.teacher = models.Teacher.objects.get(id=request.POST.get('teacher'))
        course.save()
        teachers = models.Teacher.objects.all()
        return redirect('/catalog/courses')
    elif request.method == 'GET':
        teachers = models.Teacher.objects.all()
        return render(request, 'create_course.html', {'teachers': teachers})
    
def edit_course(request, id):
    course = models.Course.objects.get(id=id)
    if request.method == 'POST':
        course.name = request.POST.get('name')
        course.description = request.POST.get('description')
        course.teacher = models.Teacher.objects.get(id=request.POST.get('teacher'))
        course.save()
        return redirect('/catalog/courses')
    elif request.method == 'GET':
        course_form = CourseForm(data=course.__dict__)
        return render(request, 'edit_course.html', {'course_form': course_form, "course_id": id})
    
def delete_course(_, id):
    course = models.Course.objects.get(id=id)
    course.delete()
    return redirect('/catalog/courses')

@permission_required('Catalog.add_teacher')
def create_teacher(request):
    if request.method == 'POST':
        form= TeacherForm(request.POST)
        if(form.is_valid()):
            teacher = models.Teacher()
            teacher.name = form.cleaned_data['name']
            teacher.email = form.cleaned_data['email']
            teacher.save()
            return redirect('/catalog/teachers')
        else:
            return render(request, 'create_teacher.html', {'form': form})
    elif request.method == 'GET':
        form = TeacherForm()
        return render(request, 'create_teacher.html', {'form': form})

def edit_teacher(request, id):
    teacher = models.Teacher.objects.get(id=id)
    if request.method == 'POST':
        form= TeacherForm(request.POST)
        if(form.is_valid()):
            teacher.name = form.cleaned_data['name']
            teacher.email = form.cleaned_data['email']
            teacher.save()
            return redirect('/catalog/teachers')
     
    elif request.method == 'GET':
        teacher_form = TeacherForm(data=teacher.__dict__)
        return render(request, 'edit_teacher.html', {'teacher_form': teacher_form, "teacher_id": id})
    

def delete_teacher(_, id):
    teacher = models.Teacher.objects.get(id=id)
    teacher.delete()
    return redirect('/catalog/teachers')