from django import forms
from .models import Teacher, Course, Batch, Student, Attendance, FeePayment


class DateInput(forms.DateInput):
    input_type = 'date'


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'email', 'phone', 'subject', 'qualification', 'joining_date']
        widgets = {'joining_date': DateInput()}


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'duration', 'fee']


class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['name', 'course', 'teacher', 'timing']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'address', 'course', 'batch', 'status', 'photo']


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']
        widgets = {'date': DateInput()}


class FeePaymentForm(forms.ModelForm):
    class Meta:
        model = FeePayment
        fields = ['student', 'amount', 'date', 'mode', 'remarks']
        widgets = {'date': DateInput()}


class StudentSearchForm(forms.Form):
    q = forms.CharField(required=False, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Search students by name, email or phone...'}
    ))
