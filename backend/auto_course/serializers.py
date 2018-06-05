from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework import status
from django.db import transaction
from rest_framework.relations import ManyRelatedField

from .models import *
from rest_framework.exceptions import APIException, ParseError, NotFound
from rest_framework.decorators import api_view
from rest_framework.response import Response

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassRoom
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = '__all__'

class TimetableSerializer(serializers.ModelSerializer):

    class Meta:
        model = course_teacher_time_classroom_relation
        fields = '__all__'
