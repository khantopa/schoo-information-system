from django.urls import path,include
from.import views

app_name = 'schools'

urlpatterns = [


    path('administration/',views.AdminIndex.as_view(),name='admin_index'),
    path('teacher/new/',views.TeacherCreateView.as_view(),name='teacher_new'),
    path('teacher/',views.TeacherListView.as_view(),name='teacher_list'),
    path('teacher/<int:pk>/',views.TeacherDetailView.as_view(),name="teacher_detail"),
    path('teacher/<int:pk>/edit/',views.TeacherUpdateView.as_view(),name='teacher_edit'),
    path('teacher/<int:pk>/remove/',views.TeacherDeleteView.as_view(),name='teacher_delete'),
    path('class/new',views.ClassesCreateView.as_view(),name='class_new'),
    path('class/',views.ClassesListView.as_view(),name='class_list'),
    path('class/<int:pk>/',views.ClassesDetailView.as_view(),name="class_detail"),
    path('class/<int:pk>/remove/',views.ClassesDeleteView.as_view(),name='class_delete'),
    path('class/<int:pk>/edit/',views.ClassesUpdateView.as_view(),name='class_edit'),
    path('student/new/',views.StudentCreateView.as_view(),name='student_new'),
    path('student/',views.StudentListView.as_view(),name='student_list'),
    path('student/<int:pk>/',views.StudentDetailView.as_view(),name="student_detail"),
    path('student/<int:pk>/edit',views.StudentUpdateView.as_view(),name='student_edit'),
    path('student/<int:pk>/remove',views.StudentDeleteView.as_view(),name='student_delete'),

]
