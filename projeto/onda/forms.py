from django import forms
from .models import AppHome, AppMonitoramento, Feed, Noticia
from django.forms import ModelForm

class AppMonitoramentoForm(forms.ModelForm):
    class Meta:
        model = AppMonitoramento
        fields = '__all__' 

class AppHomeForm(forms.ModelForm):
    class Meta:
        model = AppHome
        fields = '__all__' 

class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = '__all__' 
    
class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__' 