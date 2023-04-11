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
        quizID = request.POST["quizIDinput"]
        quizInstance = Quiz.objects.get(field_objId=quizID)
        questionList = quizInstance.field_questionList
        # 取得選取的questionId
        selected_options = request.POST.getlist('group')

        for i in selected_options:
            questionList.append(i)
        quizInstance.field_questionList = questionList
        quizInstance.save()
        
    return redirect('/showAllQuestion/')