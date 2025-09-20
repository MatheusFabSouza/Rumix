
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "rumix"

urlpatterns = [
    path("", views.inicio, name="index"),             # <- nome "index"
    path("feed/", views.feed_lista, name="feed_lista"),
    path("feed/<int:id>/", views.feed_detalhe, name="feed_detalhe"),
    path("animais/", views.animais_lista, name="animais_lista"),
    path("animais/<int:id>/", views.animal_detalhe, name="animal_detalhe"),
    path("fazendas/", views.fazendas_lista, name="fazendas_lista"),
    path("fazendas/<int:id>/", views.fazenda_detalhe, name="fazenda_detalhe"),
    path("leiloes/", views.leiloes_lista, name="leiloes_lista"),
    path("leiloes/<int:id>/", views.leilao_detalhe, name="leilao_detalhe"),
    path("perfil/", views.perfil, name="perfil"),
    path("sobre/", views.sobre, name="sobre"),
    path('login/', views.login_cadastro, name='login_cadastro'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
