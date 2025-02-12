from Catalog.models import Course, Teacher
from Catalog.serializers import CourseSerializer, TeacherSerializer
from rest_framework import viewsets, permissions


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CourseSerializer