from django.urls import path
from . import views

app_name = 'rumix'

urlpatterns = [
    path('', views.inicio, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('sobre/', views.sobre, name='sobre'),
]
