from django.urls import path
from . import views

app_name = 'fazendas'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('novo/', views.criar, name='criar'),
    path('<int:id>/', views.detalhe, name='detalhe'),
    path('<int:id>/editar/', views.editar, name='editar'),
    path('<int:id>/excluir/', views.excluir, name='excluir'),
]
