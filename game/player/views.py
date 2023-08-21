from django.shortcuts import render
from .models import Draconido, Elfo, Enano, Gnomo, Humano, Mediano, Semielfo, Semiorco, Tiefling

def mostrar_razas(request):
    razas = {
        'Draconido': Draconido.objects.all(),
        'Elfo': Elfo.objects.all(),
        'Enano': Enano.objects.all(),
        'Gnomo': Gnomo.objects.all(),
        'Humano': Humano.objects.all(),
        'Mediano': Mediano.objects.all(),
        'Semielfo': Semielfo.objects.all(),
        'Semiorco': Semiorco.objects.all(),
        'Tiefling': Tiefling.objects.all(),
    }
    return render(request, 'mostrar_razas.html', {'razas': razas})
