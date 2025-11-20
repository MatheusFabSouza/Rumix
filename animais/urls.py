from django.urls import path
from . import views

app_name = 'animais'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('novo/', views.cadastrar, name='cadastrar'),
    path('<int:id>/', views.detalhe, name='detalhe'),
    path('<int:id>/editar/', views.editar, name='editar'),
    path('<int:id>/excluir/', views.excluir, name='excluir'),
]
