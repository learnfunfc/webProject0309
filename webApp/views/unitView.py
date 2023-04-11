
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
from django.utils.safestring import mark_safe

# 進入編輯unit網頁儲存資料庫和html file
def editUnit(request, courseName=None):
    if request.method == "POST" and courseName:  # 如果是表單傳來的資料
        
        upLoadForm = CreateUnitForm(
            request.POST)  # use form.py產生 form
        course = TeachCourse.objects.get(field_name=courseName)

        if upLoadForm.is_valid():
            

            name = request.POST["name"].strip()
            discript = request.POST["descript"]
            html = request.POST["html_text"]
            

            unintOfinstance = TeachCourseUnit.objects.create(
                teach_course=course, field_name=name, field_description=discript, field_html=html)
            unintOfinstance.save()
            return redirect("/editunit/"+courseName)
    else:
        # 不是表單傳來的post就產生表單
        form = CreateUnitForm(request.POST)
        course = TeachCourse.objects.get(field_name=courseName)
        allunit = course.teachcourseunit_set.all()  # 注意此寫法

    return render(request, "showUnit.html", {"form": form, "courseName": courseName, "allObject": allunit})


def showUnitContent(request, pkId):
    content = TeachCourseUnit.objects.get(id = pkId)
    htmltext = content.field_html
    htmltext = mark_safe(htmltext)
    return HttpResponse(htmltext)
   