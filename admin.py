from django.contrib import admin
from .models import (
    Register,
    Post,
    Student,
    Course,
    Enrollment,
    Staff,
    Management,
    ClearanceItem,
    ClearanceRequest,
    NoDueCertificate,
)


# =====================================================
# ADMIN HEADER
# =====================================================

admin.site.site_header = "No Due Management System"
admin.site.site_title = "No Due Admin"
admin.site.index_title = "Dashboard"


# =====================================================
# REGISTER
# =====================================================

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'first_name',
        'last_name'
    ]

    search_fields = [
        'username',
        'email'
    ]


# =====================================================
# POST
# =====================================================

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'content'
    ]

    search_fields = [
        'title'
    ]


# =====================================================
# STUDENT
# =====================================================

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'roll_no',
        'first_name',
        'last_name',
        'email',
        'department',
        'year'
    ]

    list_filter = [
        'department',
        'year'
    ]

    search_fields = [
        'roll_no',
        'first_name',
        'last_name',
        'email'
    ]

    ordering = [
        'roll_no'
    ]


# =====================================================
# COURSE
# =====================================================

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'code',
        'name',
        'credits'
    ]

    search_fields = [
        'code',
        'name'
    ]


# =====================================================
# ENROLLMENT
# =====================================================

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = [
        'student',
        'course',
        'semester',
        'grade'
    ]

    list_filter = [
        'semester',
        'grade'
    ]

    search_fields = [
        'student__roll_no',
        'student__first_name',
        'course__code'
    ]


# =====================================================
# STAFF
# =====================================================

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = [
        'emp_id',
        'first_name',
        'last_name',
        'email',
        'department',
        'designation',
        'phone'
    ]

    list_filter = [
        'department',
        'designation'
    ]

    search_fields = [
        'emp_id',
        'first_name',
        'last_name',
        'email'
    ]


# =====================================================
# MANAGEMENT
# =====================================================

@admin.register(Management)
class ManagementAdmin(admin.ModelAdmin):
    list_display = [
        'admin_id',
        'first_name',
        'last_name',
        'email',
        'role',
        'department',
        'phone'
    ]

    list_filter = [
        'role',
        'department'
    ]

    search_fields = [
        'admin_id',
        'first_name',
        'last_name',
        'email'
    ]


# =====================================================
# CLEARANCE ITEM
# =====================================================

@admin.register(ClearanceItem)
class ClearanceItemAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'student',
        'department',
        'staff',
        'management',
        'status'
    ]

    list_filter = [
        'department',
        'status'
    ]

    search_fields = [
        'student__roll_no',
        'student__first_name',
        'department'
    ]


# =====================================================
# CLEARANCE REQUEST
# =====================================================

@admin.register(ClearanceRequest)
class ClearanceRequestAdmin(admin.ModelAdmin):
    list_display = [
        'request_id',
        'student',
        'request_date',
        'clear_date',
        'status'
    ]

    list_filter = [
        'status',
        'request_date'
    ]

    search_fields = [
        'student__roll_no',
        'student__first_name'
    ]

    ordering = [
        '-request_date'
    ]


# =====================================================
# NO DUE CERTIFICATE
# =====================================================

@admin.register(NoDueCertificate)
class NoDueCertificateAdmin(admin.ModelAdmin):
    list_display = [
        'student',
        'clearance_request',
        'certificate_no',
        'issue_date',
        'signed_by_management',
        'signed_by_staff'
    ]

    search_fields = [
        'certificate_no',
        'student__roll_no'
    ]