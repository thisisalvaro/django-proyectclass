from django.urls import path
from Catalog import views
from CatalogApi.api import CourseViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("teachers", TeacherViewSet, basename='apiTeacher')
router.register("courses", CourseViewSet, basename='apiCourse')


urlpatterns = [
    path('teachers/<int:teacher_id>/courses', views.course_by_teacher, name='course_by_teacher'),
] + router.urls


