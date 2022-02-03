from django.urls import path
from . import views

urlpatterns = [
    path('',views.fn_add, name='home'),
    path('delete/<int:taskid>/',views.fn_delete,name='delete'),
    path('update/<int:taskid>/',views.fn_update,name='update'),
    path('classbasedViewHome/',views.TaskListview.as_view(),name='classbasedViewHome'),
    path('classbasedDetailView/<int:pk>/',views.TaskDetailview.as_view(),name='classbasedDetailView'),
    path('classbasedUpdateView/<int:pk>/',views.TaskUpdateview.as_view(),name='classbasedUpdateView'),
    path('classbasedDeleteView/<int:pk>/',views.TaskDeleteView.as_view(),name='classbasedDeleteView')
]