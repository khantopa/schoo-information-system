from django import forms
from.models import Student,Classes,Teacher

class ClassesForm(forms.ModelForm):

    class Meta():
        model = Classes
        fields = ('name','section','max_students')

class StudentForm(forms.ModelForm):

    class Meta():
        model = Student
        fields = ('name','grade','date_of_birth','date_of_join','father_name','mother_name','email','profile_pic','phone','parent_phone')

class TeacherForm(forms.ModelForm):

    class Meta():
        model = Teacher
        fields = ('name','date_of_birth','email','password','profile_pic','class_teacher')
