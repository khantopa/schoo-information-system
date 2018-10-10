from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.urls import reverse_lazy,reverse
from.import models
from django.views.generic import(TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ClassesForm,StudentForm,TeacherForm


class AdminIndex(LoginRequiredMixin,TemplateView):
    template_name = 'schools/admin_index.html'

class StudentListView(LoginRequiredMixin,ListView):

    model = models.Student



class StudentDetailView(LoginRequiredMixin,DetailView):
    model = models.Student



class StudentCreateView(LoginRequiredMixin,CreateView):

    model = models.Student
    form_class = StudentForm


class StudentUpdateView(LoginRequiredMixin,UpdateView):
    model = models.Student
    template_name = 'schools/student_create_form.html'

class StudentDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Student
    template_name = 'schools/student_confirm_delete.html'


class ClassesListView(LoginRequiredMixin,ListView):

    model = models.Classes


class ClassesDetailView(LoginRequiredMixin,DetailView):
    model = models.Classes
    success_url='/thanks'

class ClassesCreateView(LoginRequiredMixin,CreateView):
    success_url='/teacher_list/'
    model = models.Classes
    form_class = ClassesForm


class ClassesUpdateView(LoginRequiredMixin,UpdateView):
    model = models.Classes
    template_name = 'schools/classes_create_form.html'

class ClassesDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Classes
    template_name = 'schools/classes_confirm_delete.html'



class TeacherListView(LoginRequiredMixin,ListView):

    model = models.Teacher


class TeacherDetailView(LoginRequiredMixin,DetailView):
    model = models.Teacher


class TeacherCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'schools/teacher_detail.html'

    form_class = TeacherForm
    model = models.Teacher



class TeacherUpdateView(LoginRequiredMixin,UpdateView):
    model = models.Teacher
    template_name = 'schools/teacher_form.html'

class TeacherDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Teacher
    template_name = 'schools/teacher_confirm_delete.html'
