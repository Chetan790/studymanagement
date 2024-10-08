from django.urls import path
from . import views

urlpatterns = [
    path('', views.study_list, name='study_list'),
    path('add/', views.add_study, name='add_study'),
    path('view/<int:pk>/', views.view_study, name='view_study'),
    path('edit/<int:pk>/', views.edit_study, name='edit_study'),
    path('delete_selected/', views.delete_selected_studies, name='delete_selected_studies'),
]
