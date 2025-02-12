from django.shortcuts import render
from Catalog.models import Course
from CatalogApi.serializers import CourseSerializer
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

@permission_classes([IsAuthepynticated])
@api_view(['GET'])
def course_by_teacher(request, teacher_id):
    courses = Course.objects.filter(teacher_id=teacher_id)
    result = CourseSerializer(courses, many=True).data
    return Response(result)
    pass