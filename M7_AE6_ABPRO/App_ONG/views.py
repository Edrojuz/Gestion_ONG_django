from django.shortcuts import render, redirect, get_object_or_404
from .models import Voluntario, Evento
from .forms import VoluntarioForm, EventoForm

def home(request):
    return render(request, 'home.html')

def crear_voluntario(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = VoluntarioForm()
    return render(request, 'App_ONG/crear_voluntario.html', {'form': form})


def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save()
            return redirect('lista')  
    else:
        form = EventoForm()
    return render(request, 'App_ONG/crear_evento.html', {'form': form})

def actualizar_voluntario(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    if request.method == 'POST':
        form = VoluntarioForm(request.POST, instance=voluntario)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = VoluntarioForm(instance=voluntario)
    return render(request, 'App_ONG/actualizar_voluntario.html', {'form': form})

def actualizar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect("lista")
    else:
        form = EventoForm(instance=evento)
    return render(request, 'App_ONG/actualizar_evento.html', {'form': form})

def lista_registros(request):
    voluntarios = Voluntario.objects.all()
    eventos = Evento.objects.all()
    return render(request, 'App_ONG/lista.html', {'voluntarios': voluntarios, 'eventos': eventos})

def eliminar_voluntario(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    if request.method == 'POST':
        voluntario.delete()
        return redirect('lista')
    return render(request, 'App_ONG/eliminar_voluntario.html', {'voluntario': voluntario, 'voluntarios': 'voluntarios'})

def eliminar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('lista')
    return render(request, 'App_ONG/eliminar_evento.html', {'evento': evento, 'eventos': 'eventos'})

def detalle_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, 'App_ONG/detalle_evento.html', {'evento': evento})

def detalle_voluntario(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    return render(request, 'App_ONG/detalle_voluntario.html', {'voluntario': voluntario})



