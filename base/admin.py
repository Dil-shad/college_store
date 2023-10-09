from django.contrib import admin
from .models import Department, Course, Purpose, Material, Profile




@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')

@admin.register(Purpose)
class PurposeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'department', 'course', 'purpose')
    list_filter = ('department', 'course', 'purpose', 'materials')
    filter_horizontal = ('materials',)
