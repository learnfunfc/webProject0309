from django.contrib import admin
from django.urls import path
from webApp import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path("show_catalog/", views.showCatalog),
    path("show_catalog/<str:courseName>/", views.showCatalog),
    path("show_course/", views.showCourse),
    path("show_course/<str:courseName>/", views.showCourse),
    path("show_unit/", views.showUnit),

    
    path("createCatalog/", views.createCatalog), 
    path("createCatalog/<str:courseName>/", views.createCatalog), 
    path("editCatalog/<int:pkId>/", views.editCatalog), 

    path("createCourse/", views.createCourse, name="creat_Course"),
    path("createCourse/<str:courseName>/", views.createCourse, name="creat_Course"),
    path("editCourse/<int:pkId>/", views.editCourse),

    path("editunit/", views.editUnit),
    path("editunit/<str:courseName>/", views.editUnit, name="create_unit"),
    path("showUnitContent/<str:fileId>/", views.showUnitContent),
    # create question url
    path('create_question/', views.create_question, name='create_question'),

    path('showAllQuestion/', views.showAllQuestion, name='showAllQuestion'),
    path('showAllQuestion/<str:quizID>/', views.showAllQuestion, name='showAllQuestion'),

    path('showAllQuiz/', views.createQuiz, name='create_quiz'),
    path('showAllQuiz/<str:quizID>/', views.createQuiz, name='create_quiz'),

    path('addQ2quiz/',views.addQuestionInQuiz),
    path("updatepage/<str:name>/<int:primaryId>/",views.updatePage),
    path("show_exam/<str:quizId>/", views.showExam),
]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

