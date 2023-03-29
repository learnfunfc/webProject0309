from django.db import models
from django.utils import timezone


class CourseCatalog(models.Model):
<<<<<<< HEAD
    CourseCatalogName = models.CharField(max_length=200)
    description = models.TextField(default="#", max_length=200)
    catalogOfpic = models.CharField(default="#", max_length=200)

    def __str__(self):
        return self.CourseCatalogName


class TeachCourse(models.Model):
    course_catalog = models.ForeignKey(CourseCatalog, on_delete=models.CASCADE)
    TeachCourseName = models.CharField(max_length=200)
    teach_description = models.TextField(max_length=200)
    teachOfpic = models.CharField(default='#', max_length=200)

    def __str__(self):
        return self.TeachCourseName
=======
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
>>>>>>> feature_quiz


class TeachCourseUnit(models.Model):
    teach_course = models.ForeignKey(TeachCourse, on_delete=models.CASCADE)
<<<<<<< HEAD
    unitName = models.CharField(max_length=200)
    unit_description = models.TextField(max_length=200, null=True)
    fileId = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.unitName

# 測驗
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    quizId = models.CharField(max_length=200,null=True)
    description = models.TextField(blank=True, null=True)
    createDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# 題目
class Question(models.Model):
    text = models.TextField()
    questionId = models.CharField(max_length=200,null=True)
    tag = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.text

#選項
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
=======
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

    def __str__(self):
        return self.field_title

# 題目
class Question(models.Model):
    field_text = models.TextField()
    field_objId = models.CharField(max_length=200,null=True)
    field_tag = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.field_text

#選項
class Choice(models.Model):
    field_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    field_text = models.CharField(max_length=200)
    field_is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.field_text
>>>>>>> feature_quiz
