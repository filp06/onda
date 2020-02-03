from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from .models import AppHome, AppMonitoramento, Feed, Noticia
from .forms import AppHomeForm, AppMonitoramentoForm, FeedForm, NoticiaForm
import json
from django.db.models import Count
from django.forms.models import model_to_dict


# Home Page.
def home(request):
	dados = {}
	dados['onda'] = AppHome.objects.all()
	dados['feeds'] = Feed.objects.all()
	titulo = AppHome.objects.values('titulo').annotate
	dados['titulo'] = titulo
	return render(request, 'onda/home.html', dados)
# Creditos Page
def sobre(request):
	dados = {}
	dados['onda'] = AppHome.objects.all()
	return render(request, 'onda/sobre.html', dados)
# Contatos Page
def contato(request):
	dados = {}
	dados['onda'] = AppHome.objects.all()
	return render(request, 'onda/contato.html', dados)
# Eteps
def etep(request):
	dados = {}
	dados['onda'] = AppHome.objects.all()
	return render(request, 'onda/etep.html', dados)
# Galeria Eteps
def galeriaEtep(request):
	dados = {}
	dados['onda'] = AppHome.objects.all()
	return render(request, 'onda/galleryEtep.html', dados)
# Fotos360
def foto360(request):
	dados = {}
	dados['onda'] = AppHome.objects.all()
	return render(request, 'onda/foto360.html', dados)
# FotosVR
def fotoVR(request):
	dados = {}
	dados['onda'] = AppHome.objects.all()
	return render(request, 'onda/fotoVR.html', dados)
# Monitoramento Page
def monitoramento(request):
	dados = {}
	dados['appms'] = AppMonitoramento.objects.all()
	return render(request, 'onda/monitoramento.html', dados)
# Noticia
def noticia(request):
	dados = {}
	dados['noticias'] = Noticia.objects.all()
	return render(request, 'onda/noticias.html', dados)
# Adimin  Page
def administrador(request):
	dados = {}
	dados['onda'] = AppHome.objects.all()
	return render(request, 'onda/administrador.html', dados)
# Lista Home Page
def lista(request):
	dados = {}
	dados['onda'] = AppHome.objects.all()
	titulo = AppHome.objects.values('titulo').annotate
	dados['titulo'] = titulo
	return render(request, 'onda/listaHome.html', dados)
# Lista Monitoramento Page
def listaM(request):
	dados = {}
	dados['appms'] = AppMonitoramento.objects.all()
	titulo = AppMonitoramento.objects.values('titulo').annotate
	dados['titulo'] = titulo
	return render(request, 'onda/listaM.html', dados)
# Lista Feed Page
def listaF(request):
	dados = {}
	dados['feeds'] = Feed.objects.all()
	titulo = Feed.objects.values('titulo').annotate
	dados['titulo'] = titulo
	return render(request, 'onda/listaF.html', dados)
# Noticias
def listaN(request):
	dados = {}
	dados['noticias'] = Noticia.objects.all()
	titulo = Noticia.objects.values('titulo').annotate
	dados['titulo'] = titulo
	return render(request, 'onda/listaN.html', dados)

##	HOME Page Add/Change/Delete Aplicações	##
@login_required
@permission_required('onda.add_app')
def aplicacoes(request):
	dados = {}
	dados['onda'] = AppHome.objects.all()
	form = AppHomeForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('url_lista_onda')
	dados['form'] = form
	return render(request, 'onda/aplicacoes.html', dados)

@login_required
@permission_required('onda.change_app')
def edita(request, pk):
	app = AppHome.objects.get(pk=pk)
	form = AppHomeForm(request.POST or None, request.FILES or None, instance=app)
	if form.is_valid():
		form.save()
		return redirect('url_lista_onda')
	dados = {}
	dados['form'] = form
	dados['app'] = app
	return render(request, 'onda/aplicacoes.html', dados)

@login_required
@permission_required('onda.delete_app')
def deleta(request, pk):
	app = AppHome.objects.get(pk=pk)
	app.delete()
	return redirect('url_lista_onda')


##	MONITORAMENTO Page Add/Change/Delete Aplicações	##
@login_required
@permission_required('onda.add_appm')
def aplicacoesM(request):
	dados = {}
	dados['appms'] = AppMonitoramento.objects.all()
	form = AppMonitoramentoForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('url_listaM_onda')
	dados['form'] = form
	return render(request, 'onda/aplicacoes.html', dados)

@login_required
@permission_required('onda.change_appm')
def editaM(request, pk):
	appm = AppMonitoramento.objects.get(pk=pk)
	form = AppMonitoramentoForm(request.POST or None, request.FILES or None, instance=appm)
	if form.is_valid():
		form.save()
		return redirect('url_listaM_onda')
	dados = {}
	dados['form'] = form
	dados['appm'] = appm
	return render(request, 'onda/aplicacoes.html', dados)

@login_required
@permission_required('onda.delete_appm')
def deletaM(request, pk):
	appm = AppMonitoramento.objects.get(pk=pk)
	appm.delete()
	return redirect('url_listaM_onda')


##	FEED Page Add/Change/Delete Aplicações	##
@login_required
@permission_required('onda.add_feed')
def aplicacoesF(request):
	dados = {}
	dados['feeds'] = Feed.objects.all()
	form = FeedForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('url_listaF_onda')
	dados['form'] = form
	return render(request, 'onda/aplicacoes.html', dados)
	
@login_required
@permission_required('onda.change_feed')
def editaF(request, pk):
	feed = Feed.objects.get(pk=pk)
	form = FeedForm(request.POST or None, request.FILES or None, instance=feed)
	if form.is_valid():
		form.save()
		return redirect('url_listaF_onda')
	dados = {}
	dados['form'] = form
	dados['feed'] = feed
	return render(request, 'onda/aplicacoes.html', dados)

@login_required
@permission_required('onda.delete_feed')
def deletaF(request, pk):
	feed = Feed.objects.get(pk=pk)
	feed.delete()
	return redirect('url_listaF_onda')


## Noticias Page Add/Change/Delete	##

@login_required
@permission_required('onda.add_noticia')
def aplicacoesN(request):
	dados = {}
	dados['noticia'] = Noticia.objects.all()
	form = NoticiaForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('url_listaN')
	dados['form'] = form
	return render(request, 'onda/notform.html', dados)

@login_required
@permission_required('onda.change_noticia')
def editaN(request, pk):
	noticia = Noticia.objects.get(pk=pk)
	form = NoticiaForm(request.POST or None, request.FILES or None, instance=noticia)
	if form.is_valid():
		form.save()
		return redirect('url_listaN')
	dados = {}
	dados['form'] = form
	dados['noticia'] = noticia
	return render(request, 'onda/notform.html', dados)

@login_required
@permission_required('onda.delete_noticia')
def deletaN(request, pk):
	noticia = Noticia.objects.get(pk=pk)
	noticia.delete()
	return redirect('url_listaN')
