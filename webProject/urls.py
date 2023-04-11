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

    
    path("createCatalog/", views.createCatalog), # 首頁/教學系統
    path("createCatalog/<str:courseName>/", views.createCatalog), # 系統目錄/教學課程 view
    path("editCatalog/<int:pkId>/", views.editCatalog), # 系統目錄/教學課程 edit save

    path("createCourse/", views.createCourse, name="creat_Course"), # course new
    path("createCourse/<str:courseName>/", views.createCourse, name="creat_Course"), # course save
    path("editCourse/<int:pkId>/", views.editCourse), # 修改course卡片外觀 edit
    path("deleteCourse/<int:pkId>/", views.deleteCourse),

    path("editunit/", views.editUnit), # 顯示單元內容
    path("editunit/<str:courseName>/", views.editUnit, name="create_unit"), # create new unit
    path("showUnitContent/<str:pkId>/", views.showUnitContent),  # view 

    # create question url
    path('create_question/', views.create_question, name='create_question'), #新增題目

    path('showAllQuestion/', views.showAllQuestion, name='showAllQuestion'),  # 題庫
    path('showAllQuestion/<str:quizID>/', views.showAllQuestion, name='showAllQuestion'),

    path('showAllQuiz/', views.createQuiz, name='create_quiz'), # 顯示所有測驗選單 所有測驗
    path('showAllQuiz/<str:quizID>/', views.createQuiz, name='create_quiz'), #

    path('addQ2quiz/',views.addQuestionInQuiz), # 匯入
    #path("updatepage/<str:name>/<int:primaryId>/",views.updatePage),
    path("show_exam/<str:quizId>/", views.showExam), # 進入  (顯示測驗題目)
]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

