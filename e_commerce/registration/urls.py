from django.urls import path
from . import views

app_name = 'registration'
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('check_old_password', views.check_old_password, name='check_old_password'),
    path('update_password', views.update_password, name='update_password'),
]