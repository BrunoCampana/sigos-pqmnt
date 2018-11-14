"""ORF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^ordemservico/escolhertipo', views.escolhertipoOS, name="escolhertipo"),
    url(r'^ordemservico/criar/(?P<tipo>\d+)/(?P<classe>\d+)/$', views.criarordemservico, name="criarordemservico"),
    url(r'^ordemservico/caixa', views.caixadeentrada, name="caixa"),
    url(r'^ordemservico/aberta', views.caixaaberta, name="aberta"),
    url(r'^ordemservico/fechada', views.caixadeencerrada, name="fechada"),
    url(r'^ordemservico/consultar', views.consultarOS, name="consulta"),
    url(r'^$', views.caixadeentrada, name="caixa"),
    url(r'^ordemservico/visualizar/(?P<os_id>\d+)/$', views.visualizarOS, name="vizOS"),
    url(r'^ordemservico/todo', views.todo, name="todo"),
]
