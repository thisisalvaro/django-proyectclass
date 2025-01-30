
from django.urls import path
from Catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path('courses/create', views.create_course, name='createCourse'),
    path('courses/<int:id>/edit', views.edit_course, name='editCourse'),
    path('courses/<int:id>/delete', views.delete_course, name='deleteCourse'),
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/create', views.create_teacher, name='createTeacher'),
    path('teachers/<int:id>/edit', views.edit_teacher, name='editTeacher'),
    path('teachers/<int:id>/delete', views.delete_teacher, name='deleteTeacher'),
]
