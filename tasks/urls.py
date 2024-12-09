from django.urls import path, include
from . import views

urlpatterns = [
    path('addTask/',views.addTask, name = 'addTask'),
    path('mark_as_done/<int:pk>',views.mark_as_done, name='mark_as_done'),
    path('delete_task/<int:pk>/',views.delete_task, name = 'delete_task'),
    path('undone/<int:pk>/',views.undone, name='undone'),
    path('edit_task/<int:pk>',views.edit_task, name='edit_task'),
]