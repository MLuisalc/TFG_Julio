from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ReportForm, SearchForm
from .models import Denuncia, DenunciaArchivo
import random
import string


def index(request):
    return render(request, 'index.html')


def canal_denuncias(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            denuncia = form.save(commit=False)
            denuncia.codigo_identificacion = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            denuncia.save()
            archivo = form.cleaned_data.get('archivo')
            if archivo:
                DenunciaArchivo.objects.create(denuncia=denuncia, archivo=archivo)
            return redirect('confirmacion_denuncia', codigo=denuncia.codigo_identificacion)
    else:
        form = ReportForm()
    return render(request, 'report.html', {'form': form})


def aviso_legal(request):
    return render(request, 'aviso_legal.html')


@login_required
def lista_denuncias(request):
    denuncias = Denuncia.objects.all()
    return render(request, 'lista_denuncias.html', {'denuncias': denuncias})


def detalle_denuncia(request, pk):
    denuncia = get_object_or_404(Denuncia, pk=pk)
    archivos = DenunciaArchivo.objects.filter(denuncia=denuncia)
    return render(request, 'detalle_denuncia.html', {'denuncia': denuncia, 'archivos': archivos})


def preguntas_frecuentes(request):
    return render(request, 'preguntas_frecuentes.html')


def normativa(request):
    return render(request, 'normativa.html')


def estado_denuncia(request):
    return render(request, 'estado_denuncia.html')


def confirmacion_denuncia(request, codigo):
    denuncia = get_object_or_404(Denuncia, codigo_identificacion=codigo)
    return render(request, 'confirmacion_denuncia.html', {'denuncia': denuncia})


def buscar_denuncia(request):
    if request.method == 'POST':
        codigo_identificacion = request.POST.get('codigo_identificacion')
        try:
            denuncia = Denuncia.objects.get(codigo_identificacion=codigo_identificacion)
            archivos = DenunciaArchivo.objects.filter(denuncia=denuncia)
            return render(request, 'detalle_denuncia.html', {'denuncia': denuncia, 'archivos': archivos})
        except Denuncia.DoesNotExist:
            return render(request, 'denuncia_no_encontrada.html', {'codigo': codigo_identificacion})
    return redirect('estado_denuncia')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def consultas(request):
    form = SearchForm(request.GET)
    denuncias = Denuncia.objects.all()
    if form.is_valid():
        numero_denuncia = form.cleaned_data.get('numero_denuncia')
        fecha_inicio = form.cleaned_data.get('fecha_inicio')
        fecha_fin = form.cleaned_data.get('fecha_fin')
        tipificacion_denuncia = form.cleaned_data.get('tipificacion_denuncia')

        if numero_denuncia:
            denuncias = denuncias.filter(codigo_identificacion__icontains=numero_denuncia)
        if fecha_inicio and fecha_fin:
            denuncias = denuncias.filter(fecha_hora__range=[fecha_inicio, fecha_fin])
        if tipificacion_denuncia:
            denuncias = denuncias.filter(tipificacion_denuncia=tipificacion_denuncia)

    return render(request, 'consultas.html', {'form': form, 'denuncias': denuncias})


@login_required
def expedientes(request):
    return render(request, 'expedientes.html')


@login_required
def informes(request):
    return render(request, 'informes.html')
