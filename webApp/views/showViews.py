from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import CourseCatalog, TeachCourseUnit, TeachCourse, Quiz, Question, Choice
from ..forms import CreateCourseForm, CreateCatalogForm, CreateUnitForm, QuestionForm, ChoiceForm,createQuizForm,CreateCatalogFormWithoutFile
from django.conf import settings
import os
import glob
from hashlib import sha256
from datetime import datetime
from .myModule import hashEncoding,save_File
import json



# present web content
def index(request):
    return render(request, "index.html", locals())


def showCatalog(request, courseName=""):
    allObject = CourseCatalog.objects.all()
    # mylocals = dict(locals()) # 用來檢查request參數
    return render(request, "showCatalog.html", locals())


def showCourse(request, courseName=""):
    allObject = TeachCourse.objects.all()
    return render(request, "showCourse.html", locals())


def showUnit(request, status=None):
    allObject = TeachCourseUnit.objects.all()  # 沒有特異性
    return render(request, "showUnit.html", locals())



def showExam(request,quizId=None):
    quizInstance = Quiz.objects.get(field_objId=quizId)
    allQuestion = quizInstance.field_questionList
    html=""
    for qId in allQuestion:
        questionInstance = Question.objects.get(field_objId= qId)
        html += "<h3>"+questionInstance.field_text+"</h3>"
        choiceInstance = Choice.objects.filter(field_question=questionInstance)
        for choice in choiceInstance:
            html += "<input type='radio' name='choice' value='"+choice.field_text+"'>"+choice.field_text+"<br>"

    return HttpResponse(html)