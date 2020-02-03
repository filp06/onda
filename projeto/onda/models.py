from django.db import models
from django.forms import ModelForm

# Model Monitoramento.
class AppMonitoramento(models.Model):
    
    titulo = models.CharField(max_length= 85, null=True)
    link = models.CharField(max_length= 250, null=True)
    descricao = models.TextField(null=True)
    imagem = models.ImageField(null=True, blank=True, upload_to='monitoramento/')

    
    def __str__(self):
        return self.titulo

# Model Home
class AppHome(models.Model):
    
    titulo = models.CharField(max_length= 85, null=True)
    link = models.CharField(max_length= 250, null=True)
    descricao = models.TextField(null=True)
    imagem = models.ImageField(null=True, blank=True, upload_to='home/')

    
    def __str__(self):
        return self.titulo

# Model Feed
class Feed(models.Model):

    titulo = models.CharField(max_length= 85, null=True)
    link = models.CharField(max_length= 250, null=True)
    descricao = models.TextField(null=True)
    imagem = models.ImageField(null=True, blank=True, upload_to='feed/')
    
    def __str__(self):
        return self.titulo
    
# Model Noticia
class Noticia(models.Model):

    titulo = models.CharField(max_length= 85, null=True)
    link = models.CharField(max_length= 250, null=True)
    descricao = models.TextField(null=True)
    imagem = models.ImageField(null=True, blank=True, upload_to='noticias/')
    criado_em = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Criado em:")
    upload_em = models.DateTimeField(auto_now=True, null=True, verbose_name="Upload em:")
    opcoesCategoria = [
        (u'Alertas de Indícios de Queimadas e Desmatamento', u'Alertas de Indícios de Queimadas e Desmatamento'),
        (u'Biblioteca Brasília Ambiental', u'Biblioteca Brasília Ambiental'),
        (u'Catálogo de Metadados', u'Catálogo de Metadados'),
        (u'Dados Abertos', u'Dados Abertos'),
        (u'ETEPs', u'ETEPs'),
        (u'Eu Amo Cerrado', u'Eu Amo Cerrado'),
        (u'Geoinformação', u'Geoinformação'),
        (u'Geoserviço', u'Geoserviço'),
        (u'Monitoramento Ambiental', u'Monitoramento Ambiental'),
        (u'Qualificação dos Alertas de Queimadas e Desmatamento', u'Qualificação dos Alertas de Queimadas e Desmatamento'),
        (u'Urutau', u'Urutau')]
    categoria = models.CharField(null=True, max_length=100, choices=opcoesCategoria)

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo