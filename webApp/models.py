from django.db import models
from django.utils import timezone
from django.db.models import JSONField

class CourseCatalog(models.Model):
    field_name = models.CharField(max_length=200)
    field_description = models.TextField(default="#", max_length=200)
    field_pic = models.CharField(default="#", max_length=200)

    def __str__(self):
        return self.field_name

class TeachCourse(models.Model):
    course_catalog = models.ForeignKey(CourseCatalog, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=200)
    field_description = models.TextField(max_length=200)
    field_pic = models.CharField(default='#', max_length=200)

    def __str__(self):
        return self.field_name


class TeachCourseUnit(models.Model):
    teach_course = models.ForeignKey(TeachCourse, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=200)
    field_description = models.TextField(max_length=200, null=True)
    field_fileId = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.field_name

# 測驗
class Quiz(models.Model):
    field_title = models.CharField(max_length=200)
    field_objId = models.CharField(max_length=200,null=True)
    field_description = models.TextField(blank=True, null=True)
    field_createDate = models.DateTimeField(default=timezone.now)
    field_tag = JSONField(default=list)
    field_questionList = JSONField(default=list)
    

    def __str__(self):
        return self.field_title

# 題目
class Question(models.Model):
    field_text = models.TextField()
    field_objId = models.CharField(max_length=200,null=True)
    field_tag = JSONField(default=list)
    def __str__(self):
        return self.field_text

#選項
class Choice(models.Model):
    field_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    field_text = models.CharField(max_length=200)
    field_is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.field_text
