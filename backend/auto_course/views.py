import django_filters
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import filters
from .serializers import *
from .models import *
from rest_framework.generics import *
from rest_framework.mixins import *
from .filters import *
# Create your views here.

@api_view(['GET','POST','PUT', 'DELETE'])
def teacher(request):
    if request.method == 'GET':
        teacher_list = Faculty.objects.all()
        serializers = TeacherSerializer(teacher_list, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassroomList(ListCreateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassroomSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter)
    filter_class = ClassroomFilter
    search_fields = ('classroom_location',)

    def post(self, request):
        serializer = ClassroomSerializer(data=request.data)
        flag = True
        if serializer.is_valid():
            roomname = request.data['classroom_location']
            capacity = int(request.data['classroom_capacity'])
            rooms = ClassRoom.objects.all()
            if capacity > 200:
                flag = False
            if flag:
                serializer.save()
                return Response({'msg': 'add successful', 'state': True}, status=status.HTTP_201_CREATED)
            else:
                return Response({'msg': 'add failed'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'msg': 'add failed'}, status=status.HTTP_400_BAD_REQUEST)


class ClassroomUpdate(RetrieveUpdateDestroyAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassroomSerializer


class CourseList(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter)
    filter_class = CourseFilter
    search_fields = ('name',)

class RequestList(ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class RequestUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class TimetableList(ListCreateAPIView):
    queryset = course_teacher_time_classroom_relation.objects.all()
    serializer_class = TimetableSerializer

class TimetableUpdate(RetrieveUpdateDestroyAPIView):
    queryset = course_teacher_time_classroom_relation.objects.all()
    serializer_class = TimetableSerializer
