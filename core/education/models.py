from django.db import models
from users.models import CustomUser

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=255)


class Group(models.Model):
    name = models.CharField(max_length=255)


class Course(models.Model):

    group_types = (
        (1, "حضوری"),
        (2, "غیر حضوری"),
    )

    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.IntegerField()
    type = models.IntegerField(choices=group_types, default=1)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)


class Participant(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
