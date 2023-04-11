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

# 儲存至資料庫
def createCatalog(request):
    if request.method == "POST":  # 如果是表單傳來的資料
        upLoadForm = CreateCatalogForm(
            request.POST, request.FILES)  # use form.py產生 form

        if upLoadForm.is_valid():
            upLoadfile = save_File(request.FILES['file'], "jpg")

            name = request.POST["name"].strip()
            discript = request.POST["descript"]
            filename = request.FILES['file'].name.split(".")[0]
            file_id = hashEncoding(filename)

            CatalogOfinstance = CourseCatalog.objects.create(
                field_name=name, field_description=discript, field_pic=file_id)
            CatalogOfinstance.save()
            return redirect("/createCatalog/")
    else:

        form = CreateCatalogForm(request.POST)
        allObject = CourseCatalog.objects.all()

    return render(request, "showCatalog.html", {"form": form,  "allObject": allObject})


# 修改Catalog內容
def editCatalog(request,pkId):
    instance = CourseCatalog.objects.get(id=pkId)
    if request.method == "POST":
        form = CreateCatalogForm(request.POST)
        if form.is_valid():
             
            catalog = CourseCatalog.objects.get(id = pkId)
            
            catalog.field_name = request.POST["name"].strip()
            catalog.field_description = request.POST["descript"]
            catalog.save()
            return redirect("/createCatalog/")

    else:
        initial_data = {
            'name': instance.field_name,
            'descript': instance.field_description,
            # 使用实例数据为其他表单字段设置初始值
        }

        form = CreateCatalogFormWithoutFile(initial=initial_data)
        allObject = CourseCatalog.objects.all()
    return render(request, "editCatalog.html", {'form': form,'pk':pkId})


def updatePage(request,name,primaryId):
    if name == "CourseCatalog":
        getInstance = CourseCatalog.objects.get(id=primaryId)
    if name == "TeachCourse":
        getInstance = TeachCourse.objects.get(id=primaryId)

    # initial_data = {
    #         'field1': getInstance.name,
    #         'field2': my_model_instance.field2,
    #     }
    return render(request,"updatepage.html",locals())
