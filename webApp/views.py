from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CourseCatalog, TeachCourseUnit, TeachCourse, Quiz, Question, Choice
from .forms import CreateCourseForm, CreateCatalogForm, CreateUnitForm, QuestionForm, ChoiceForm,createQuizForm
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

    return render(request, "showCourse.html", {"form": form, "allObject": allunit})


def showUnitContent(request, fileId):
    target = os.path.join(settings.BASE_DIR, "webApp",
                          "templates2", fileId + '.html')
    with open(target, "r", encoding="utf-8") as file:
        content = file.read()

    return render(request, "showUnitContent.html", locals())


# 進入編輯unit網頁儲存資料庫和html file
def editUnit(request, courseName=None):
    if request.method == "POST" and courseName:  # 如果是表單傳來的資料
        upLoadForm = CreateUnitForm(
            request.POST, request.FILES)  # use form.py產生 form
        course = TeachCourse.objects.get(field_name=courseName)

        if upLoadForm.is_valid():
            upLoadfile = save_File(request.FILES['file'], "html")

            name = request.POST["name"].strip()
            discript = request.POST["descript"]
            filename = request.FILES['file'].name.split(".")[0]
            file_id = hashEncoding(filename)

            unintOfinstance = TeachCourseUnit.objects.create(
                teach_course=course, field_name=name, field_description=discript, field_fileId=file_id)
            unintOfinstance.save()
            return redirect("/editunit/"+courseName)
    else:
        # 不是表單傳來的post就產生表單
        form = CreateUnitForm(request.POST)
        course = TeachCourse.objects.get(field_name=courseName)
        allunit = course.teachcourseunit_set.all()  # 注意此寫法

    return render(request, "showUnit.html", {"form": form, "courseName": courseName, "allObject": allunit})


# -------------------question-------------------


def create_question(request):
    if request.method == 'POST':
        
        form = QuestionForm(request.POST, num_choices=4)
        tags_str = request.POST.get('field_tag', '')
        tags_json = json.dumps(tags_str.split(', '))
        request.POST._mutable = True
        request.POST['field_tag'] = tags_json
        request.POST._mutable = False
        
        if form.is_valid():
            question = form.save(commit=False)
            
            current_time = datetime.now()
            nowTimeString = current_time.strftime("%Y%m%d%H%M%S")
            id = hashEncoding(nowTimeString)[:6]
            question.field_objId = id
            question.save()
            
            """ 使用 enumerate 函數獲取當前選擇表單的索引。
                然後，我們使用從 request.POST 提交的數據以及相應的前綴來初始化每個 choice_form。
                這樣，驗證函數將使用提交的數據對每個 choice_form 進行驗證，然後正確地保存 choice。 """
            for i, choice_form in enumerate(form.choice_forms):
                # Initialize choice form with submitted POST data

                choice_form = ChoiceForm(request.POST, prefix=f'choice_{i}')
                if choice_form.is_valid():

                    choice = choice_form.save(commit=False)
                    choice.field_question = question
                    
                    choice.save()
        return redirect('/showAllQuestion/')
        
    else:
        form = QuestionForm(num_choices=4)  # 創建一個空的 QuestionForm 實例，等待用戶提交表單

    return render(request, 'create_question.html', {'form': form, 'choice_forms': form.choice_forms})

# 取得資料庫中所有question或者該 quiz的所有question
def showAllQuestion(request,quizID=None):
    # if quizID:
    #     quizInstance = Quiz.objects.get(field_objId=quizID)
    allQuestion = Question.objects.all()
    return render(request, "showAllQuestion.html", locals())


def createQuiz(request):
    allQuiz = Quiz.objects.all()

    if request.method == 'POST':
        form = createQuizForm(request.POST)
        if form.is_valid():
            name = request.POST["name"].strip()
            discript = request.POST["descript"]
            my_list = request.POST["my_list"]
           
            my_list = my_list.split(',')
            my_list = [item.strip() for item in my_list]
            json_list = json.dumps(my_list)
            
            current_time = datetime.now()
            nowTimeString = current_time.strftime("%Y%m%d%H%M%S")
            hashId = hashEncoding(nowTimeString)[:6]
            quizOfinstance = Quiz.objects.create(field_title=name, field_description = discript,field_objId = hashId,field_tag = json_list)
            quizOfinstance.save()
            return redirect('/showAllQuiz/')
    else:
        form = createQuizForm()
        context = {"form":form, "allQuiz":allQuiz}
    
    return render(request, "showAllQuiz.html", context)


def addQuestionInQuiz(request):
    if request.method == "POST":
        print(request.POST)
    return redirect('/showAllQuestion/')


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

