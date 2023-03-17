from django.db import models
from django.utils import timezone


class CourseCatalog(models.Model):
    CourseCatalogName = models.CharField(max_length=200)
    description = models.TextField(default="#", max_length=200)
    fileId = models.CharField(default="#", max_length=200)
    def __str__(self):
        return self.CourseCatalogName
    

class TeachCourse(models.Model):
    course_catalog = models.ForeignKey(CourseCatalog, on_delete=models.CASCADE)
    TeachCourseName = models.CharField(max_length=200)
    teach_description = models.TextField(max_length=200)
    fileId = models.CharField(default='#', max_length=200)
    

    def __str__(self):
        return self.TeachCourseName
    

class TeachCourseUnit(models.Model):
    teach_course = models.ForeignKey(TeachCourse, on_delete=models.CASCADE)
    unitName = models.CharField(max_length=200)
    unit_description = models.TextField(max_length=200,null=True)
    fileId = models.CharField(max_length=200,null=True)

    
    def __str__(self):
        return self.unitName