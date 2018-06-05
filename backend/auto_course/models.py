from django.db import models
from authentication.models import *

# Create your models here.


class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Faculty, related_name='request_tid', on_delete=models.CASCADE)
    content = models.TextField()
    statue = models.IntegerField()

class ClassRoom(models.Model):
    classroom_id = models.AutoField(primary_key=True)
    classroom_location = models.CharField("地点", max_length=50, unique=True);
    classroom_capacity = models.IntegerField("容量", null=False);

class course_teacher_time_classroom_relation(models.Model):
    time = models.CharField("时间", max_length=5)
    teacher = models.ForeignKey(Faculty,related_name="timetable_tid", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="timetable_cid", on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom,related_name="timetable_rid", on_delete=models.CASCADE)

