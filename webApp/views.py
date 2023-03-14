from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CourseCatalog, TeachCourseUnit, TeachCourse
from .forms import EditCourseForm

from django.conf import settings
from uuid_upload_path import uuid # not used
import os
import glob
from hashlib import sha256 


'''
todo
1. add edit forms on the modal
2. add breadcrum function 
'''

# 呈現網頁目前內容
def index(request):
    return render(request, "index.html", locals())

# status用來呈現alter畫面 提醒使用者已經完成新增
def showCatalog(request, status=None): # 不帶有參數的url的寫法 
    allObject = CourseCatalog.objects.all()
    return render(request, "showCatalog.html", locals())

def showCourse(request, status=None): 
    allObject= TeachCourse.objects.all()
    return render(request, "showCourse.html", locals())

def showUnit(request,status=None):
    allObject = TeachCourseUnit.objects.all()
    return render(request, "showUnit.html", locals())



# 進入新增網頁表單 deprecation!!!
def newCatalog(request):
    return render(request, "newcata.html", locals())

def newCourse(request):
    return render(request, "newcourse.html", locals())
##### deprecation!!!

# 儲存至資料庫
def createCatalog(request):
    if request.method == 'POST':
        name = request.POST["name"].strip()
        descript = request.POST["descript"]
        catalog = CourseCatalog.objects.create(CourseCatalogName=name, description=descript)
        allNameOfCatalog = CourseCatalog.objects.all()
        catalog.save()
        contextDict = locals()

        if catalog: # 成功建立實體
            return redirect("/show_catalog/success/") # 返回預覽畫面
        
        return redirect("/show_catalog/")


def createCourse(request):
    if request.method == 'POST':
        name = request.POST["name"].strip()
        descript = request.POST["descript"]
        course_catalog = CourseCatalog.objects.get(name)
        course = TeachCourse.objects.create(course_catalog=course_catalog,TeachCourseName=name, description=descript)
        course.save()
        if course:
            return redirect("/show_course/success/") # 返回預覽畫面
        return redirect("/show_course/")


# 進入編輯unit網頁儲存資料庫和html file
def editUnit(request):
    if request.method == "POST":
        upLoadForm = EditCourseForm(request.POST,request.FILES)
        name = request.POST["name"].strip()
        descript = request.POST["descript"]
        course = TeachCourse.objects.get(name)
        unit = TeachCourse.objects.create(teach_course=course,unitName=name, description=descript)
        course.save()
        if upLoadForm.is_valid():
            upLoadfile = save_htmlFile(request.FILES['file'])
            unit_name = request.POST["unitName"].strip()
            unit_discript = request.POST["content"]
            file_id = hashEncoding(request.FILES['file'].name)
            unintOfinstance = TeachCourseUnit.objects.create(unitName=unit_name,unit_description=unit_discript,fileId= file_id)
            unintOfinstance.save()
            return redirect("/show_catalog/")
        
    else:
        form  = EditCourseForm(request.POST)

    return render(request, "editcourse.html", {"form": form})

def save_htmlFile(f):
    filename = f.name
    filename = filename.split(".")[0] #remove file extention
    
    target = os.path.join(settings.BASE_DIR,"webApp","media", hashEncoding(filename) +'.html')
    with open(target,'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        
    return os.path.basename(target)

def hashEncoding(filename,length=15):
    nameut8 = filename.encode('utf-8')
    hashValue = sha256(nameut8).hexdigest()
    return hashValue[:length]