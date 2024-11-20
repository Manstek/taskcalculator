from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_input_view, name='task_input'),  # Страница для ввода данных
    path('<int:pk>/', views.view_task, name='view_task'),
    path('<int:pk>/res/', views.calculate_costs_with_check, name='costs')
]
