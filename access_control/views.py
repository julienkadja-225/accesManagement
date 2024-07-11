from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import User, Application, Role, Permission, UserRole, RolePermission

@login_required
def dashboard(request):
    return render(request, 'access_control/dashboard.html')

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'access_control/user_list.html', {'users': users})

@login_required
def application_list(request):
    applications = Application.objects.all()
    return render(request, 'access_control/application_list.html', {'applications': applications})

@login_required
def role_list(request):
    roles = Role.objects.all()
    return render(request, 'access_control/role_list.html', {'roles': roles})

@login_required
def permission_list(request):
    permissions = Permission.objects.all()
    return render(request, 'access_control/permission_list.html', {'permissions': permissions})

# Ajoutez des vues pour ajouter, modifier et supprimer des utilisateurs, applications, rôles et permissions
