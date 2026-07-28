from django.contrib import admin
from .models import Teacher, Course, Batch, Student, Attendance, FeePayment


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'joining_date')
    search_fields = ('name', 'email', 'subject')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'fee')
    search_fields = ('name',)


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'teacher', 'timing')
    list_filter = ('course',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'course', 'batch', 'status', 'admission_date')
    list_filter = ('status', 'course', 'batch')
    search_fields = ('name', 'email', 'phone')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status')
    list_filter = ('status', 'date')


@admin.register(FeePayment)
class FeePaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount', 'date', 'mode')
    list_filter = ('mode', 'date')
