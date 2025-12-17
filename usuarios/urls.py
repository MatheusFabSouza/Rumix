from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path("login/",auth_views.LoginView.as_view(template_name="registration/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(template_name="registration/logged_out.html"),name="logout"),
    path("register/", views.cadastrar_usuario, name="register"),
    path("password_change/",auth_views.PasswordChangeView.as_view(template_name="registration/password_change_form.html"),name="password_change"),
    path("password_change/done/",auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html"),name="password_change_done"),
    path("password_change/done/",auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html"),name="password_change_done"),
    path("password_reset/",auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),name="password_reset"),
    path("password_reset/done/",auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),name="password_reset_done"),
    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),name="password_reset_confirm"),
    path("reset/done/",auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),name="password_reset_complete"),
    path("", views.usuarios, name="usuarios"),
    path("novo/", views.usuarios_novo, name="usuarios_novo"),
    path("<int:id>/detalhar/", views.usuarios_detalhar, name="usuarios_detalhar"),
    path("<int:id>/editar/", views.usuarios_editar, name="usuarios_editar"),
    path("<int:id>/remover/", views.usuarios_remover, name="usuarios_remover"),
    path("perfil/", views.perfil, name="perfil"),
    path("perfil/editar/", views.editar_perfil, name="editar_perfil"),
]
