
from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import CourseCatalog, TeachCourseUnit, TeachCourse, Quiz, Question, Choice
from ..forms import CreateCourseForm, CreateCatalogForm, CreateUnitForm, QuestionForm, ChoiceForm,createQuizForm,CreateCatalogFormWithoutFile,CreateCourseFormithoutFile
from django.conf import settings
import os
import glob
from hashlib import sha256
from datetime import datetime
from .myModule import hashEncoding,save_File
import json


def createCourse(request, courseName=None):
    
    if request.method == "POST" and courseName:  # 如果是表單傳來的資料
        
        upLoadForm = CreateCourseForm(
            request.POST, request.FILES)  # use form.py產生 form
        course = CourseCatalog.objects.get(field_name=courseName)
        if upLoadForm.is_valid():
            upLoadfile = save_File(request.FILES['file'], "jpg")

            name = request.POST["name"].strip()
            discript = request.POST["descript"]
            filename = request.FILES['file'].name.split(".")[0]
            file_id = hashEncoding(filename)

            CourseOfinstance = TeachCourse.objects.create(
                course_catalog=course, field_name=name, field_description=discript, field_pic=file_id)
            CourseOfinstance.save()
            return redirect("/createCourse/"+courseName)
    else:
        # 不是表單傳來的post就產生表單

        form = CreateCourseForm(request.POST)
        course = CourseCatalog.objects.get(field_name=courseName)
        allunit = course.teachcourse_set.all()  # 注意此寫法

    return render(request, "showCourse.html", {"form": form, "allObject": allunit,"courseName":courseName})


# 修改Course卡片內容
def editCourse(request,pkId):
    instance = TeachCourse.objects.get(id=pkId)
    if request.method == "POST":
        form = CreateCourseForm(request.POST)
        if form.is_valid():
             
            course= TeachCourse.objects.get(id = pkId)
            
            course.field_name = request.POST["name"].strip()
            course.field_description = request.POST["descript"]
            fk = course.course_catalog
            course.save()
            return redirect("/createCourse/"+fk.field_name)

    else:
        initial_data = {
            'name': instance.field_name,
            'descript': instance.field_description,
            
        }

        form = CreateCourseFormithoutFile(initial=initial_data)
        allObject = TeachCourse.objects.all()
    return render(request, "editCourse.html", {'form': form,'pk':pkId})


def deleteCourse(request,pkId):
    instance = TeachCourse.objects.get(pk=pkId)
    instance.delete()
    return redirect("/createCatalog/")

