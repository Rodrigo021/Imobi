from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Imovel, Cidade, Visitas
from django.shortcuts import get_object_or_404


#verificando se o usuário está logado, caso não esteja logado será redirecionado para página de login
@login_required(login_url='/auth/login')
def home(request):
    preco_minimo = request.GET.get('preco_minimo')
    preco_maximo = request.GET.get('preco_maximo')
    cidade = request.GET.get('cidade')
    tipo = request.GET.getlist('tipo')
    cidades = Cidade.objects.all()

    imoveis = Imovel.objects.all()

    if preco_minimo:
        imoveis = imoveis.filter(valor__gte=preco_minimo)

    if preco_maximo:
        imoveis = imoveis.filter(valor__lte=preco_maximo)

    if cidade:
        imoveis = imoveis.filter(cidade=cidade)

    if tipo:
        imoveis = imoveis.filter(tipo_imovel__in=tipo)
 
    return render(request, 'home.html', {'imoveis': imoveis, 'cidades': cidades})

def imovel(request, id):
    imovel = get_object_or_404(Imovel, id=id)
    sugestoes = Imovel.objects.filter(cidade=imovel.cidade).exclude(id=id)[:2]
    return render(request, 'imovel.html', {'imovel': imovel, 'sugestoes': sugestoes, 'id': id})

def agendar_visitas(request):
    usuario = request.user
    dia = request.POST.get('dia')
    horario = request.POST.get('horario')
    id_imovel = request.POST.get('id_imovel')

    visita = Visitas(
        imovel_id = id_imovel,
        usuario = usuario,
        dia = dia,
        horario = horario
    )
    visita.save()

    return redirect('/agendamentos')

def agendamentos(request):
    visitas = Visitas.objects.filter(usuario=request.user)
    return render(request, 'agendamentos.html', {'visitas': visitas})

def cancelar_agendamento(request, id):
    visitas = get_object_or_404(Visitas, id=id)
    visitas.status = "C"
    visitas.save()
    return redirect('/agendamentos')

def sair(request):
    auth.logout(request)
    return redirect('./auth/login')
 