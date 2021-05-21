from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

from django.db.models.fields import DateTimeField

# Create your models here.

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    _id = models.AutoField(primary_key=True, editable=False)
    name =  models.CharField(max_length=200, null=True, blank=True)
    subscribtionFee = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    monthlyFee = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    hasPersonalTrainingFee = models.BooleanField(default=False)
    personalTrainingFee = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    totalFee =  models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    beginingDate = DateTimeField(models.DateTimeField(auto_now_add=True))
    #image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Instructor(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    firstName =  models.CharField(max_length=200, null=True, blank=True)
    lastName =  models.CharField(max_length=200, null=True, blank=True)
    speciality =  models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class PersonalClass(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    fitnessGoal =  models.CharField(max_length=200, null=True, blank=True)
    musculeTrained = models.CharField(max_length=200, null=True, blank=True)
    level = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)


    def __str__(self):
        return self.name

class GroupClass(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True)
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    level = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    category =  models.CharField(max_length=200, null=True, blank=True)
    capacity = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)


    def __str__(self):
        return self.name


class WorkoutSession(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    personalClass = models.ForeignKey(PersonalClass, on_delete=models.SET_NULL,null=True)
    groupClass =  models.ForeignKey(GroupClass, on_delete=models.SET_NULL,null=True)
    workoutNumber = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    duration = models.DurationField(default=timedelta(minutes=40))
    startTime = models.TimeField()
    endTime = models.TimeField()
    date = models.DateTimeField()
    room = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name


