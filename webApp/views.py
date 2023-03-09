from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CourseCatalog
from .forms import EditCourseForm
'''
todo
1. add a function which can create new course and this course can bind to Catalog 
user can press "add new course" button and then web page will show a form.
2. optional: admin can edit the content of teaching materials at back-end.
'''



def index(request):
    return render(request, "index.html", locals())



def showCatalog(request, status=None): # 不帶有參數的url的寫法
    allNameOfCatalog = CourseCatalog.objects.all()
    print(status)

    return render(request, "usercatalog.html", locals())


def newCatalog(request):
    print(request)
    return render(request, "newcata.html", locals())


def createCatalog(request):
    if request.method == 'POST':
        courseName = request.POST["course_name"].strip()
        descripts = request.POST["course_descript"]
        catalog = CourseCatalog.objects.create(CourseCatalogName=courseName, description=descripts)
        allNameOfCatalog = CourseCatalog.objects.all()
        contextDict = locals()

        if catalog:
            return redirect("/show_catalog/success/")

        return redirect("/show_catalog/")


def EditCourse(request):
    form  = EditCourseForm(request.POST)
    return render(request, "editcourse.html", {"form": form})