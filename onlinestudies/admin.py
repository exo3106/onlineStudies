from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Instructor) 
class InstructorAdmin(admin.ModelAdmin):
     list_display = ['instructor_name ']
     
admin.site.register(Category) 
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Course) 
class CoursesAdmin(admin.ModelAdmin):
    list_display = [    
        'category',
        'course_name',
        'description',
        'instructor',
        'skills',
        ' univesity',
        'instructor_id'
        ]
    list_filter = ['in_stock','is_active']
    prepopulated_fileld = {'slug':('course_name',)}
