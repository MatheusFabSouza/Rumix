from django.urls import path
from . import views

app_name = 'animais'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('editar/<int:pk>/', views.editar, name='editar'),
    path('excluir/<int:pk>/', views.excluir, name='excluir'),
    path('detalhe/<int:pk>/', views.detalhe, name='detalhe'),
]

