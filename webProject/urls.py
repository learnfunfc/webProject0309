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
    path("show_unit", views.showUnit),

    path("newcatalog/", views.newCatalog),
    path("createCatalog/", views.createCatalog),
    path("newcourse/", views.newCatalog),
    path("createCourse/", views.createCourse),


    path("editunit/", views.editUnit),

]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
