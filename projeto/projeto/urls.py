from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from onda.views import (home, sobre, aplicacoes, aplicacoesM, 
monitoramento, administrador, edita, deleta, lista, editaM, deletaM,
 listaM, listaF, editaF, deletaF, aplicacoesF, noticia, listaN, aplicacoesN,
 deletaN, editaN, contato, etep, galeriaEtep, foto360, fotoVR)
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Páginas Principais
    path('', home, name='url_home_onda'),
    path('sobre/', sobre, name='url_sobre'),
    path('contatos/', contato, name='url_contato'),
    path('administrador/', administrador, name='url_administrador_onda'),
    path('monitoramento/', monitoramento, name='url_monitoramento_onda'),
    # Django Admin/Accounts
    path('admin/', admin.site.urls, name='url_admin'),
    path('login/', auth_views.LoginView.as_view(), name='url_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='url_logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    # Aplicações Home
    path('lista_home/', lista, name='url_lista_onda'),
    path('adicionar_aplicacoes_home/', aplicacoes, name='url_aplicacoes_onda'),
    path('editar_app_home/<int:pk>/', edita, name='url_edita_app'),
    path('deletar_app_home/<int:pk>/', deleta, name='url_deleta_app'),
    # Aplicações Monitoramento
    path('lista_monitoramento/', listaM, name='url_listaM_onda'),
    path('adicionar_aplicacoes_monitoramento/', aplicacoesM, name='url_aplicacoesM_onda'),
    path('editar_app_monitoramento/<int:pk>/', editaM, name='url_edita_appM'),
    path('deletar_app_monitoramento/<int:pk>/', deletaM, name='url_deleta_appM'),
    # Aplicações Feed
    path('lista_feed/', listaF, name='url_listaF_onda'),
    path('adicionar_aplicacoes_feed/', aplicacoesF, name='url_aplicacoesF_onda'),
    path('editar_app_feed/<int:pk>/', editaF, name='url_edita_feed'),
    path('deletar_app_feed/<int:pk>/', deletaF, name='url_deleta_feed'),
    # Noticias
    path('ultimas_noticias/', noticia, name='url_noticia'),
    path('lista_noticia/', listaN, name='url_listaN'),
    path('adicionar_aplicacoes_noticia/', aplicacoesN, name='url_aplicacoesN'),
    path('editar_app_noticia/<int:pk>/', editaN, name='url_edita_noticia'),
    path('deletar_app_noticia/<int:pk>/', deletaN, name='url_deleta_noticia'),
    #
    path('etep/', etep, name='url_etep'),
    path('galeria/', galeriaEtep, name='url_galeria'),
    path('imagem360/', foto360, name='url_foto360'),
    path('realidade_virtual/', fotoVR, name='url_fotoVR'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
