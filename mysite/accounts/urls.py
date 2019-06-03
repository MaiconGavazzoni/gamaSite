from django.urls import path
from django.contrib.auth import views as auth_views
#from .views import register, dashboard, edit, edit_password, password_reset, password_reset_confirm

app_name = 'accounts'

urlpatterns = [

    path('entrar/', auth_views.LoginView.as_view
        (template_name='accounts/entrar.html'), name='login'),
    path('sair/', auth_views.LogoutView.as_view
        (template_name='index.html'), name='logout'),
]