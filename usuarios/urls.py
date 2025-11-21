from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from rumix import views as rumix_views

app_name = 'usuarios'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.cadastrar_usuario, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', views.usuarios, name='usuarios'),
    path('novo/', views.usuarios_novo, name='usuarios_novo'),
    path('<int:id>/detalhar/', views.usuarios_detalhar, name='usuarios_detalhar'),
    path('<int:id>/editar/', views.usuarios_editar, name='usuarios_editar'),
    path('<int:id>/remover/', views.usuarios_remover, name='usuarios_remover'),
    path("perfil/", views.perfil, name="perfil"),
    path("perfil/editar/", views.editar_perfil, name="editar_perfil"),
]