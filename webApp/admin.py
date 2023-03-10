from django.contrib import admin
from .models import CourseCatalog, TeachCourse, TeachCourseUnit
# Register your models here.
admin.site.register(CourseCatalog)
admin.site.register(TeachCourse)
admin.site.register(TeachCourseUnit)
