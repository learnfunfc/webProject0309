from django.contrib import admin
from django.urls import path
from webApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path("show_catalog/", views.showCatalog),
    path("show_catalog/<str:status>/", views.showCatalog),
    path("newcatalog/", views.newCatalog),
    path("createCatalog/", views.createCatalog),
    path("editcourse/", views.EditCourse),

]
