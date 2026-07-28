from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    qualification = models.CharField(max_length=150)
    joining_date = models.DateField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50, help_text='e.g. 6 Months, 1 Year')
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Batch(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='batches')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='batches')
    timing = models.CharField(max_length=100, help_text='e.g. Mon-Fri 6-8 PM')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.course.name})'


class Student(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255, blank=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='students')
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    admission_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)

    class Meta:
        ordering = ['-admission_date']

    def __str__(self):
        return self.name

    @property
    def total_paid(self):
        return sum(p.amount for p in self.payments.all())

    @property
    def balance_due(self):
        if self.course:
            return self.course.fee - self.total_paid
        return 0


class Attendance(models.Model):
    STATUS_CHOICES = (
        ('present', 'Present'),
        ('absent', 'Absent'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='present')

    class Meta:
        ordering = ['-date']
        unique_together = ('student', 'date')

    def __str__(self):
        return f'{self.student.name} - {self.date} - {self.status}'


class FeePayment(models.Model):
    MODE_CHOICES = (
        ('cash', 'Cash'),
        ('online', 'Online'),
        ('cheque', 'Cheque'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    mode = models.CharField(max_length=10, choices=MODE_CHOICES, default='cash')
    remarks = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.student.name} - {self.amount}'
