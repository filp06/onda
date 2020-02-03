from django.contrib import admin
from .models import AppHome, AppMonitoramento, Feed, Noticia
# Register your models here.

admin.site.register(AppMonitoramento)

admin.site.register(AppHome)

admin.site.register(Feed)

admin.site.register(Noticia)