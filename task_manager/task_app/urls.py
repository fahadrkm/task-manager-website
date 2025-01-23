from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # View for the task list
    path('add/', views.add_task, name='add_task'),  # View to add a task
    path('update/<int:task_id>/', views.update_task, name='update_task'),  # View to update a task
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # View to delete a task
    path('register/', views.register_user, name='register'),  # View for user registration
    path('login/', views.login_user, name='login'),  # View for user login
    path('logout/', views.logout_user, name='logout'),  # View for user logout
     path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
]
