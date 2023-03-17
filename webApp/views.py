from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CourseCatalog, TeachCourseUnit, TeachCourse
from .forms import CreateUnitForm, CreateCatalogForm, CreateCourseForm
from django.conf import settings
from uuid_upload_path import uuid  # not used
import os
import glob
from hashlib import sha256


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


# 儲存至資料庫
# refactor createCatalog
def createCatalog(request, courseName=None):
    if request.method == "POST" and courseName:  # 如果是表單傳來的資料
        upLoadForm = CreateCatalogForm(
            request.POST, request.FILES)

        if upLoadForm.is_valid():
            upLoadfile = save_htmlFile(request.FILES['file'])
            name = request.POST["name"].strip()
            discript = request.POST["descript"]
            filename = request.FILES['file'].name.split(".")[0]
            file_id = hashEncoding(filename)

            CatalogOfinstance = CourseCatalog.objects.create(
                CourseCatalogName=name, description=discript, fileId=file_id)
            CatalogOfinstance.save()
            return redirect("/show_catalog/"+courseName)

    else:
        # 不是表單傳來的post就產生表單
        form = CreateCatalogForm(request.POST)
        allObject = CourseCatalog.objects.all()

    return render(request, "showCatalog.html", {"form": form, "courseName": courseName, "allObject": allObject})

#!! breadcrum can't work 
def createCourse(request, courseName=None):
    if request.method == "POST" and courseName:
        upLoadForm = CreateCourseForm(
            request.POST, request.FILES)
        course = CourseCatalog.objects.get(CourseCatalogName=courseName)

        if upLoadForm.is_valid():
            upLoadfile = save_htmlFile(request.FILES['file'], "html")
            name = request.POST["name"].strip()
            discript = request.POST["descript"]
            filename = request.FILES['file'].name.split(".")[0]
            file_id = hashEncoding(filename)

            courseOfinstance = TeachCourse.objects.create(
                course_catalog=course, TeachCourseName=name, teach_description=discript, fileId=file_id)
            courseOfinstance.save()
            return redirect("/createCourse/"+courseName)

    else:
        # 不是表單傳來的post就產生表單
        form = CreateUnitForm()
        course = CourseCatalog.objects.get(CourseCatalogName=courseName) # 取得上一個FK
        allunit = course.teachcourse_set.all()  # 注意此寫法

    return render(request, "showCourse.html", {"form": form, "courseName": courseName, "allObject": allunit})


# 進入編輯unit網頁儲存資料庫和html file
def editUnit(request, courseName=None):

    if request.method == "POST" and courseName:  # 如果是表單傳來的資料
        upLoadForm = CreateUnitForm(
            request.POST, request.FILES)  # use form.py產生 form
        course = TeachCourse.objects.get(TeachCourseName=courseName)

        if upLoadForm.is_valid():
            upLoadfile = save_htmlFile(request.FILES['file'], "html")
            name = request.POST["name"].strip()
            discript = request.POST["descript"]
            filename = request.FILES['file'].name.split(".")[0]
            file_id = hashEncoding(filename)

            unintOfinstance = TeachCourseUnit.objects.create(
                teach_course=course, unitName=name, unit_description=discript, fileId=file_id)
            unintOfinstance.save()
            return redirect("/editunit/"+courseName)

    else:
        # 不是表單傳來的post就產生表單
        form = CreateUnitForm(request.POST)
        course = TeachCourse.objects.get(TeachCourseName=courseName)
        allunit = course.teachcourseunit_set.all()  # 注意此寫法

    return render(request, "showUnit.html", {"form": form, "courseName": courseName, "allObject": allunit})


def save_htmlFile(f, fileType):
    filename = f.name
    filename = filename.split(".")[0]  # remove file extention

    target = os.path.join(settings.BASE_DIR, "webApp",
                          "media", hashEncoding(filename) + "." + fileType)
    with open(target, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return os.path.basename(target)


def hashEncoding(filename, length=15):
    nameut8 = filename.encode('utf-8')
    hashValue = sha256(nameut8).hexdigest()
    return hashValue[:length]
