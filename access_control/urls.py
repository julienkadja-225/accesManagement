from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('users/', views.user_list, name='user_list'),
    path('applications/', views.application_list, name='application_list'),
    path('roles/', views.role_list, name='role_list'),
    path('permissions/', views.permission_list, name='permission_list'),
    # Ajoutez des URLs pour ajouter, modifier et supprimer des utilisateurs, applications, rôles et permissions
]
