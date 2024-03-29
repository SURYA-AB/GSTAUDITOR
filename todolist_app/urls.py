from django.urls import path
from todolist_app import views
from django.contrib import admin  

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('complete/<task_id>', views.complete_task, name='complete_task'),
    path('pending/<task_id>', views.pending_task, name='pending_task'),

]
handler404 = todolist_app.views.handler404
handler500 = todolist_app.views.handler500
