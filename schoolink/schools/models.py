from django.db import models
# import PhoneField
import datetime
from django.urls import reverse


class Student(models.Model):


    profile_pic = models.ImageField()
    grade = models.ForeignKey('Classes',on_delete=models.CASCADE)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=datetime.datetime.today)
    father_name = models.CharField(blank=True, max_length=100)
    mother_name = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=100)
    parent_phone = models.CharField(blank=True, max_length=100)
    date_of_join = models.DateField(default=datetime.datetime.today)
    last_login = models.DateField(default=datetime.datetime.today)
    # attendance = models.ForeignKey('Attendance',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("student_detail",kwargs={'pk':self.pk})


class Teacher(models.Model):

    profile_pic = models.ImageField(blank=True)
    email = models.EmailField(blank=True)
    password = models.CharField(blank=True, max_length=100)
    name = models.CharField(blank=True, max_length=100)
    date_of_birth = models.DateField(default=datetime.datetime.today)
    class_teacher = models.ForeignKey('Classes',on_delete=models.CASCADE)
    last_login = models.DateField(blank=True,default=datetime.datetime.today)
    # attendance = models.ForeignKey('Attendance',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("teacher_detail",kwargs={'pk':self.pk})

class Classes(models.Model):

    name = models.CharField(blank=True, max_length=100)
    section = models.CharField(blank=True,max_length=100)
    max_students = models.IntegerField()


    def __str__(self):
        return (self.name,self.section)



class TeachersSubject(models.Model):
    teacher= models.ForeignKey('Teacher',on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject',on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher

class Subject(models.Model):

    name = models.CharField(blank=True, max_length=100)
    level = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    date = models.DateField(default=datetime.datetime.today)
    student = models.ForeignKey('Student',on_delete=models.CASCADE)
    grade = models.ForeignKey('Classes',on_delete=models.CASCADE)
    present = models.BooleanField(default=True)
    remark = models.TextField(blank=True)

    def __str__(self):
        return (self.student,self.grade)

class ExamType(models.Model):

    name = models.CharField(blank=True, max_length=100)
    desc = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.name

class Exam(models.Model):

    exam_type = models.ForeignKey('ExamType',on_delete=models.CASCADE)
    name = models.CharField(blank=True, max_length=100)
    start_date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.name

class ExamResult(models.Model):
    exam = models.ForeignKey('Exam', on_delete=models.CASCADE)
    student = models.ForeignKey('Student',on_delete=models.CASCADE)
    grade = models.ForeignKey('Classes',on_delete=models.CASCADE)
    marks = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return (self.student,self.grade)
