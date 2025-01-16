
# Create your views here.

#from django import http
from django.shortcuts import render

from Catalog import models

def index(request,id):
   # return http.HttpResponse("Heloo, word . You are at the Catalog index")
   #course = ['curse1','curse2','curse3']
   courses = models.Course.objects.all()
   return render(request , 'index.html' , {'identificator' : id  , 'courses' : courses})