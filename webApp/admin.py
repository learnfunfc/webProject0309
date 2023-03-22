from django.contrib import admin
from .models import CourseCatalog, TeachCourse, TeachCourseUnit, Quiz,Question,Choice
# Register your models here.
admin.site.register(CourseCatalog)
admin.site.register(TeachCourse)
admin.site.register(TeachCourseUnit)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
