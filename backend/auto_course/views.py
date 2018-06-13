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
    search_fields = ('campus', 'building', 'room',)


    def post(self, request):
        serializer = ClassroomSerializer(data=request.data)
        print(request.data)

        flag = True
        if serializer.is_valid():
            campus = request.data['campus']
            building = request.data['building']
            room = request.data['room']
            location = campus + building + room
            capacity = int(request.data['capacity'])
            rooms = ClassRoom.objects.all()
            for everyroom in rooms:
                existlocation = everyroom.get_campus_display() + everyroom.building + everyroom.room
                if(location == existlocation):
                    flag = False
            if capacity > 200:
                flag = False
            if flag:
                serializer.save()
                return Response({'msg': 'add successful', 'state': True}, status=status.HTTP_201_CREATED)
            else:
                return Response({'msg': 'add failed'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'msg': 'add failed'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        classrooms = self.filter_queryset(self.get_queryset())
        serializer = ClassroomSerializer(classrooms, many=True)
        response = {
            "name": "RoomResources",
            "rooms": serializer.data
        }
        return Response(response)


class ClassroomUpdate(RetrieveUpdateDestroyAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassroomSerializer

    def put(self, request, pk):
        classroom = ClassRoom.objects.get(pk=pk)
        serializer = ClassroomSerializer(classroom, data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'add successful', 'state': True}, status=status.HTTP_201_CREATED)
        else:
            return Response({'msg': 'add failed'}, status=status.HTTP_400_BAD_REQUEST)



class CourseList(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter)
    filter_class = CourseFilter
    search_fields = ('name',)

class RequestList(ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def get(self, request, *args, **kwargs):
        requstlist = Request.objects.all()
        serializer = RequestSerializer(requstlist, many=True)
        response = {
            "name": "Notifications",
            "notifications": serializer.data
        }
        return Response(response)

    def post(self, request):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'add successful', 'state': True}, status=status.HTTP_201_CREATED)
        return Response({'msg': 'add failed'}, status=status.HTTP_400_BAD_REQUEST)

class RequestUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def put(self, request, pk):
        updaterequest = Request.objects.get(pk=pk)
        serializer = RequestSerializer(updaterequest, data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response({'msg': 'add successful', 'state': True}, status=status.HTTP_201_CREATED)
        else:
            return Response({'msg': 'add failed'}, status=status.HTTP_400_BAD_REQUEST)

class TimetableList(ListCreateAPIView):
    queryset = course_teacher_time_classroom_relation.objects.all()
    serializer_class = TimetableSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter)
    filter_class = TimetableFilter
    search_fields = ('teachername',)

    def get(self, request, *args, **kwargs):
        classrooms = self.filter_queryset(self.get_queryset())
        serializer = TimetableSerializer(classrooms, many=True)
        response = {
            "name": "CourseResources",
            "courses": serializer.data
        }
        return Response(response)



class TimetableUpdate(RetrieveUpdateDestroyAPIView):
    queryset = course_teacher_time_classroom_relation.objects.all()
    serializer_class = TimetableSerializer

    def put(self, request, pk):
        changecourse = course_teacher_time_classroom_relation.objects.get(pk=pk)
        serializer = TimetableSerializer(changecourse, data=request.data)
        flag = True
        if serializer.is_valid():
            print(request.data)
            for everyroom in ClassRoom.objects.all():
                name = everyroom.get_campus_display() + everyroom.building + everyroom.room
                if name == request.data['room']:
                    newroom = everyroom
                    break
            # check capacity
            course_capacity = Course.objects.get(pk=request.data['course_id']).capacity
            new_capacity = newroom.classroom_capacity
            if new_capacity < course_capacity:
                flag = False
                error = "too small room"
            # check classroom
            newtime = request.data['time']
            newroomname = newroom.get_campus_display() + newroom.building + newroom.room
            for everytimetable in course_teacher_time_classroom_relation.objects.all():
                if everytimetable.classroom.get_campus_display() + everytimetable.classroom.building + everytimetable.classroom.room == newroomname:
                    if everytimetable.time == newtime:
                        flag = False
                        error = "classroom comflicts!"
            #check teacher time
            for everytimetable in course_teacher_time_classroom_relation.objects.all():
                currentteacher = Faculty.objects.get(pk=request.data['teacher_username'])
                if everytimetable.teacher == currentteacher:
                    if everytimetable.time == request.data['time'] and everytimetable != changecourse:
                        flag = False
                        error = "Teacher already has course!"
            if flag:
                serializer.save()
                return Response({'msg': 'add successful', 'state': True}, status=status.HTTP_201_CREATED)
            else:
                return Response({'msg': 'add successful', 'state': error}, status=status.HTTP_201_CREATED)
        else:
            return Response({'msg': 'add failed'}, status=status.HTTP_400_BAD_REQUEST)

