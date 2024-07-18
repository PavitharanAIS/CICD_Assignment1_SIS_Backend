from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Programme(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Marks(models.Model):
    programmeMarks = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.programmeMarks


class Parents(models.Model):
    fatherName = models.CharField(max_length=100)
    motherName = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fatherName


class TuitionFee(models.Model):
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, related_name='programmeId')
    tuitionFee = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tuitionFee


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    address = models.CharField(max_length=100)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, related_name='programme')
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, related_name='lecturer')
    marks = models.ForeignKey(Marks, on_delete=models.CASCADE, related_name='marks')
    parents = models.ForeignKey(Parents, on_delete=models.CASCADE, related_name='parents')
    tuitionFee = models.ForeignKey(TuitionFee, on_delete=models.CASCADE, related_name='fee')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
