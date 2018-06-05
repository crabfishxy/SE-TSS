import django_filters
from .models import *
from .serializers import  *

class ClassroomFilter(django_filters.rest_framework.FilterSet):

    id = django_filters.CharFilter(name="classroom_id")

    class Meta:
        model = ClassRoom
        fields = ['id']

class CourseFilter(django_filters.rest_framework.FilterSet):

    id = django_filters.CharFilter(name="course_id")

    class Meta:
        model = Course
        fields = ['id']