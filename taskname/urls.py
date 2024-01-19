from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolist_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', todolist_views.index1a, name='index1a'),
    #path('', todolist_views.indexapi, name='indexapi'),
    #path('mul/', todolist_views.FileFieldView, name='FileFieldView'),
    #path('2a', todolist_views.index2a, name='index2a'),
    path('', todolist_views.gst, name='gst'),
    #path('handler500',todolist_views.handler500,name='handler500'),
    #path('handler404',todolist_views.handler404,name='handler404'),
    path('handler500',todolist_views.handler500,name='handler500'),
]
