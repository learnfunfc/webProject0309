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
    if quizID:
        # 取得quiz實體
        quizInstance = Quiz.objects.get(field_objId=quizID)
        # 取得quiz 問題列表
        allQuestion = quizInstance.field_questionList
        
        print(allQuestion)
    else:
        # 輸出資料庫中所有問題表單
        allQuestion = Question.objects.all()
    return render(request, "showAllQuestion.html", locals())
