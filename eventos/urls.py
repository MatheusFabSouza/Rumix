from django.urls import path
from . import views

app_name = "eventos"

urlpatterns = [
    path("", views.pagina_eventos, name="index"),
    path("table/", views.tabela_eventos, name="table_partial"),
    path("create/", views.criar_evento, name="create_ajax"),
    path("edit/<int:pk>/", views.editar_evento, name="edit_ajax"),
    path("delete/<int:pk>/", views.excluir_evento, name="delete_ajax"),
    path("detail/<int:pk>/", views.detalhe_evento, name="detail_ajax"),
    path("ajax-messages/", views.mensagens_ajax, name="ajax_messages"),
]
