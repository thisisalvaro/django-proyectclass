
# Create your views here.

#from django import http
from django.shortcuts import redirect, render

from Catalog import models
from Catalog.forms import TeacherForm

def index(request):
   # return http.HttpResponse("Heloo, word . You are at the Catalog index")
   #course = ['curse1','curse2','curse3']
   
   #{'identificator' : id  , 'courses' : courses}
   courses = models.Course.objects.all()
   return render(request , 'index.html')

def create_course(request):
    if request.method == 'POST':
        name=request.POST.get('description')
        description=request.POST.get('description')
        teacher_id=request.POST.get('teacher')
        teacher = models.Teacher.objects.get(pk=teacher_id)
        course = models.Course(name=name, description=description, teacher=teacher)
        course.save()
        return redirect('/catalog')
    else:
         teachers = models.Teacher.objects.all()
         return render(request , 'create_course.html' , {'teachers': teachers})

def create_teacher(request):
    
      if request.method == 'POST':
         form = TeacherForm(request.POST)
         if form.is_valid():
               form.save()
               return redirect('/catalog')
         else:
               return render(request , 'create_teacher.html' , {'form': form})
      else:
         form = TeacherForm()
         return render(request , 'create_teacher.html' , {'form': form})
      
def edit_teacher(request, id):
    return render(request , 'edit_teacher.html')