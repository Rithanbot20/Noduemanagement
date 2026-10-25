from django.db import models


# =====================================================
# REGISTER
# =====================================================

class Register(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=30)
    address = models.TextField(max_length=1000)

    class Meta:
        verbose_name_plural = "Registers"

    def __str__(self):
        return self.username


# =====================================================
# POST
# =====================================================

class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(max_length=3000)

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title


# =====================================================
# STUDENT
# =====================================================

class Student(models.Model):
    roll_no = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    year = models.IntegerField()
    address = models.TextField()
    password = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.roll_no} - {self.first_name} {self.last_name}"


# =====================================================
# COURSE
# =====================================================

class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    credits = models.IntegerField()

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return f"{self.code} - {self.name}"


# =====================================================
# ENROLLMENT
# =====================================================

class Enrollment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    semester = models.CharField(max_length=10)

    grade = models.CharField(
        max_length=2,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"

    def __str__(self):
        return f"{self.student.roll_no} - {self.course.code}"


# =====================================================
# STAFF
# =====================================================

class Staff(models.Model):
    emp_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"

    def __str__(self):
        return f"{self.emp_id} - {self.first_name} {self.last_name}"


# =====================================================
# MANAGEMENT
# =====================================================

class Management(models.Model):
    admin_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50)

    department = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Management"
        verbose_name_plural = "Management"

    def __str__(self):
        return f"{self.admin_id} - {self.first_name} {self.last_name}"


# =====================================================
# CLEARANCE ITEM
# =====================================================

class ClearanceItem(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Cleared', 'Cleared'),
        ('Not Cleared', 'Not Cleared'),
    ]

    DEPARTMENT_CHOICES = [
        ('Library', 'Library'),
        ('Bursary', 'Bursary / Fees'),
        ('Hostel', 'Hostel'),
        ('Department', 'Department'),
        ('Sports', 'Sports'),
        ('Placement', 'Placement Cell'),
        ('Exam Cell', 'Exam Cell'),
        ('Lab', 'Lab Equipment'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='clearance_items'
    )

    department = models.CharField(
        max_length=20,
        choices=DEPARTMENT_CHOICES
    )

    staff = models.ForeignKey(
        Staff,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    management = models.ForeignKey(
        Management,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    class Meta:
        verbose_name = "Clearance Item"
        verbose_name_plural = "Clearance Items"

    def __str__(self):
        return f"{self.student.roll_no} - {self.department} - {self.status}"


# =====================================================
# CLEARANCE REQUEST
# =====================================================

class ClearanceRequest(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Rejected', 'Rejected'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    request_id = models.AutoField(
        primary_key=True
    )

    request_date = models.DateTimeField(
        auto_now_add=True
    )

    clear_date = models.DateTimeField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    class Meta:
        verbose_name = "Clearance Request"
        verbose_name_plural = "Clearance Requests"

    def __str__(self):
        return f"{self.student.roll_no} - {self.status}"


# =====================================================
# NO DUE CERTIFICATE
# =====================================================

class NoDueCertificate(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    clearance_request = models.OneToOneField(
        ClearanceRequest,
        on_delete=models.CASCADE
    )

    certificate_no = models.CharField(
        max_length=20,
        unique=True
    )

    issue_date = models.DateTimeField(
        auto_now_add=True
    )

    signed_by_management = models.ForeignKey(
        Management,
        on_delete=models.SET_NULL,
        null=True
    )

    signed_by_staff = models.ForeignKey(
        Staff,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "No Due Certificate"
        verbose_name_plural = "No Due Certificates"

    def __str__(self):
        return f"Certificate - {self.student.roll_no}"