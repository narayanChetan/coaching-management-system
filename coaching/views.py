from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q, Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Teacher, Course, Batch, Student, Attendance, FeePayment
from .forms import (
    TeacherForm, CourseForm, BatchForm, StudentForm,
    AttendanceForm, FeePaymentForm, StudentSearchForm,
)


@login_required
def dashboard(request):
    total_students = Student.objects.count()
    active_students = Student.objects.filter(status='active').count()
    total_teachers = Teacher.objects.count()
    total_courses = Course.objects.count()
    total_batches = Batch.objects.count()
    total_fees_collected = FeePayment.objects.aggregate(total=Sum('amount'))['total'] or 0
    recent_students = Student.objects.all()[:5]
    recent_payments = FeePayment.objects.select_related('student').all()[:5]

    context = {
        'total_students': total_students,
        'active_students': active_students,
        'total_teachers': total_teachers,
        'total_courses': total_courses,
        'total_batches': total_batches,
        'total_fees_collected': total_fees_collected,
        'recent_students': recent_students,
        'recent_payments': recent_payments,
    }
    return render(request, 'coaching/dashboard.html', context)


# ---------- Student Views ----------

class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'coaching/student_list.html'
    context_object_name = 'students'
    paginate_by = 10

    def get_queryset(self):
        queryset = Student.objects.select_related('course', 'batch').all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(email__icontains=query) | Q(phone__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = StudentSearchForm(self.request.GET or None)
        return context


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'coaching/student_form.html'
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        messages.success(self.request, 'Student added successfully.')
        return super().form_valid(form)


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'coaching/student_form.html'
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        messages.success(self.request, 'Student updated successfully.')
        return super().form_valid(form)


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'coaching/confirm_delete.html'
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        messages.success(self.request, 'Student deleted successfully.')
        return super().form_valid(form)


# ---------- Teacher Views ----------

class TeacherListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'coaching/teacher_list.html'
    context_object_name = 'teachers'
    paginate_by = 10


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'coaching/teacher_form.html'
    success_url = reverse_lazy('teacher_list')

    def form_valid(self, form):
        messages.success(self.request, 'Teacher added successfully.')
        return super().form_valid(form)


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'coaching/teacher_form.html'
    success_url = reverse_lazy('teacher_list')

    def form_valid(self, form):
        messages.success(self.request, 'Teacher updated successfully.')
        return super().form_valid(form)


class TeacherDeleteView(LoginRequiredMixin, DeleteView):
    model = Teacher
    template_name = 'coaching/confirm_delete.html'
    success_url = reverse_lazy('teacher_list')

    def form_valid(self, form):
        messages.success(self.request, 'Teacher deleted successfully.')
        return super().form_valid(form)


# ---------- Course Views ----------

class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'coaching/course_list.html'
    context_object_name = 'courses'
    paginate_by = 10


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'coaching/course_form.html'
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        messages.success(self.request, 'Course added successfully.')
        return super().form_valid(form)


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'coaching/course_form.html'
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        messages.success(self.request, 'Course updated successfully.')
        return super().form_valid(form)


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'coaching/confirm_delete.html'
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        messages.success(self.request, 'Course deleted successfully.')
        return super().form_valid(form)


# ---------- Batch Views ----------

class BatchListView(LoginRequiredMixin, ListView):
    model = Batch
    template_name = 'coaching/batch_list.html'
    context_object_name = 'batches'
    paginate_by = 10


class BatchCreateView(LoginRequiredMixin, CreateView):
    model = Batch
    form_class = BatchForm
    template_name = 'coaching/batch_form.html'
    success_url = reverse_lazy('batch_list')

    def form_valid(self, form):
        messages.success(self.request, 'Batch added successfully.')
        return super().form_valid(form)


class BatchUpdateView(LoginRequiredMixin, UpdateView):
    model = Batch
    form_class = BatchForm
    template_name = 'coaching/batch_form.html'
    success_url = reverse_lazy('batch_list')

    def form_valid(self, form):
        messages.success(self.request, 'Batch updated successfully.')
        return super().form_valid(form)


class BatchDeleteView(LoginRequiredMixin, DeleteView):
    model = Batch
    template_name = 'coaching/confirm_delete.html'
    success_url = reverse_lazy('batch_list')

    def form_valid(self, form):
        messages.success(self.request, 'Batch deleted successfully.')
        return super().form_valid(form)


# ---------- Attendance Views ----------

class AttendanceListView(LoginRequiredMixin, ListView):
    model = Attendance
    template_name = 'coaching/attendance_list.html'
    context_object_name = 'attendances'
    paginate_by = 15

    def get_queryset(self):
        return Attendance.objects.select_related('student').all()


class AttendanceCreateView(LoginRequiredMixin, CreateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = 'coaching/attendance_form.html'
    success_url = reverse_lazy('attendance_list')

    def form_valid(self, form):
        messages.success(self.request, 'Attendance recorded successfully.')
        return super().form_valid(form)


class AttendanceDeleteView(LoginRequiredMixin, DeleteView):
    model = Attendance
    template_name = 'coaching/confirm_delete.html'
    success_url = reverse_lazy('attendance_list')

    def form_valid(self, form):
        messages.success(self.request, 'Attendance record deleted.')
        return super().form_valid(form)


# ---------- Fee Payment Views ----------

class FeePaymentListView(LoginRequiredMixin, ListView):
    model = FeePayment
    template_name = 'coaching/fee_list.html'
    context_object_name = 'payments'
    paginate_by = 15

    def get_queryset(self):
        return FeePayment.objects.select_related('student').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_collected'] = FeePayment.objects.aggregate(total=Sum('amount'))['total'] or 0
        return context


class FeePaymentCreateView(LoginRequiredMixin, CreateView):
    model = FeePayment
    form_class = FeePaymentForm
    template_name = 'coaching/fee_form.html'
    success_url = reverse_lazy('fee_list')

    def form_valid(self, form):
        messages.success(self.request, 'Fee payment recorded successfully.')
        return super().form_valid(form)


class FeePaymentDeleteView(LoginRequiredMixin, DeleteView):
    model = FeePayment
    template_name = 'coaching/confirm_delete.html'
    success_url = reverse_lazy('fee_list')

    def form_valid(self, form):
        messages.success(self.request, 'Fee payment record deleted.')
        return super().form_valid(form)
