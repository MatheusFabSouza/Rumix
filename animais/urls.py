from django.urls import path
from . import views

app_name = 'animais'

urlpatterns = [
    path('', views.lista, name='lista'),  # nome correto: 'lista'
    path('novo/', views.cadastrar, name='cadastrar'),
    path('<int:pk>/', views.detalhe, name='detalhe'),
    path('<int:pk>/editar/', views.editar, name='editar'),
    path('<int:pk>/excluir/', views.excluir, name='excluir'),
]
