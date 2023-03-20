from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CourseCatalog, TeachCourseUnit, TeachCourse
from .forms import CreateCourseForm, CreateCatalogForm, CreateUnitForm
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
    if request.method == "POST" :  # 如果是表單傳來的資料
        upLoadForm = CreateCatalogForm(
            request.POST, request.FILES)  # use form.py產生 form
        
        if upLoadForm.is_valid():
                upLoadfile = save_File(request.FILES['file'],"jpg")
                
                name = request.POST["name"].strip()
                discript = request.POST["descript"]
                filename = request.FILES['file'].name.split(".")[0]
                file_id = hashEncoding(filename)
                
                CatalogOfinstance = CourseCatalog.objects.create(
                CourseCatalogName=name, description=discript, catalogOfpic=file_id)
                CatalogOfinstance.save()
                return redirect("/createCatalog/")      
    else:
          
        form = CreateCatalogForm(request.POST)
        allObject = CourseCatalog.objects.all()
       

    return render(request, "showCatalog.html", {"form": form,  "allObject": allObject})




def createCourse(request,courseName=None):
    if request.method == "POST" and courseName:  # 如果是表單傳來的資料
        upLoadForm = CreateCourseForm(
            request.POST, request.FILES)  # use form.py產生 form
        course = CourseCatalog.objects.get(CourseCatalogName=courseName)
        if upLoadForm.is_valid():
                upLoadfile = save_File(request.FILES['file'],"jpg")
                
                name = request.POST["name"].strip()
                discript = request.POST["descript"]
                filename = request.FILES['file'].name.split(".")[0]
                file_id = hashEncoding(filename)
                
                CourseOfinstance = TeachCourse.objects.create(
                course_catalog=course,TeachCourseName=name, teach_description=discript, teachOfpic=file_id)
                CourseOfinstance.save()
                return redirect("/createCourse/"+courseName)      
    else:
        # 不是表單傳來的post就產生表單
        
        form = CreateCourseForm(request.POST)
        course = CourseCatalog.objects.get(CourseCatalogName=courseName)
        allunit = course.teachcourse_set.all() # 注意此寫法

    return render(request, "showCourse.html", {"form": form, "allObject": allunit})





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
        upLoadForm = CreateUnitForm(
            request.POST, request.FILES)  # use form.py產生 form
        course = TeachCourse.objects.get(TeachCourseName=courseName)

        if upLoadForm.is_valid():
            upLoadfile = save_File(request.FILES['file'],"html")
           
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
        allunit = course.teachcourseunit_set.all() # 注意此寫法

    return render(request, "showUnit.html", {"form": form, "courseName": courseName, "allObject": allunit})


def save_File(f,filetype):
    filename = f.name
    filename = filename.split(".")[0]  # remove file extention
    if filetype=="html":
        target = os.path.join(settings.BASE_DIR, "webApp",
                            "templates2", hashEncoding(filename) + "."+ filetype)
    if filetype=="jpg":
        target = os.path.join(settings.BASE_DIR,
                            "media", hashEncoding(filename) + "."+ filetype)
        
    with open(target, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return os.path.basename(target) # 回傳檔名.副檔名


def hashEncoding(filename, length=15):
    nameut8 = filename.encode('utf-8')
    hashValue = sha256(nameut8).hexdigest()
    return hashValue[:length]
