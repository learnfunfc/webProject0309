from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CourseCatalog, TeachCourseUnit, TeachCourse
from .forms import EditCourseForm
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
def createCatalog(request):
    if request.method == 'POST':
        name = request.POST["name"].strip()
        descript = request.POST["descript"]
        catalog = CourseCatalog.objects.create(
            CourseCatalogName=name, description=descript)
        allNameOfCatalog = CourseCatalog.objects.all()
        catalog.save()

        # check whether instance is created??
        # if catalog: # 成功建立實體
        #     return redirect("/show_catalog/") # 返回預覽畫面

        return redirect("/show_catalog/")


def createCourse(request):
    if request.method == 'POST':

        name = request.POST["name"].strip()
        descript = request.POST["descript"]
        courseName = request.GET.get("p")
        print(courseName)
        course_catalog = CourseCatalog.objects.get(
            CourseCatalogName=courseName)
        course = TeachCourse.objects.create(
            course_catalog=course_catalog, TeachCourseName=name, teach_description=descript)
        course.save()
        # if course:
        #     return redirect("/show_course/") # 返回預覽畫面
        return redirect("/show_course/")


def showUnitContent(request,fileId):
    target = os.path.join(settings.BASE_DIR, "webApp",
                          "templates2", fileId + '.html')
    with open(target,"r",encoding="utf-8") as file:
        content = file.read()
    
    return render(request,"showUnitContent.html",locals())
    #return HttpResponse(content)


# 進入編輯unit網頁儲存資料庫和html file
def editUnit(request, courseName=None):  
    if request.method == "POST" and courseName:  # 如果是表單傳來的資料
        upLoadForm = EditCourseForm(
            request.POST, request.FILES)  # use form.py產生 form
        course = TeachCourse.objects.get(TeachCourseName=courseName)

        if upLoadForm.is_valid():
            upLoadfile = save_htmlFile(request.FILES['file'])
            print(upLoadfile)
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
        form = EditCourseForm(request.POST)
        course = TeachCourse.objects.get(TeachCourseName=courseName)
        allunit = course.teachcourseunit_set.all() # 注意此寫法

    return render(request, "showUnit.html", {"form": form, "courseName": courseName, "allObject": allunit})


def save_htmlFile(f):
    filename = f.name
    filename = filename.split(".")[0]  # remove file extention

    target = os.path.join(settings.BASE_DIR, "webApp",
                          "templates2", hashEncoding(filename) + '.html')
    
    with open(target, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return os.path.basename(target) # 回傳檔名.副檔名


def hashEncoding(filename, length=15):
    nameut8 = filename.encode('utf-8')
    hashValue = sha256(nameut8).hexdigest()
    return hashValue[:length]
