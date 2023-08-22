from django.shortcuts import render
from .models import Draconido, Elfo, Enano, Gnomo, Humano, Mediano, Semielfo, Semiorco, Tiefling
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    # Tu lógica de vista aquí
    return render(request, 'home.html')  

def logout_view(request):
    logout(request)
    messages.success(request, '¡Has cerrado sesión correctamente!')
    return redirect('home')  # Cambia 'home' al nombre de tu vista de inicio
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '¡Inicio de sesión exitoso!')
            return redirect('home')  # Cambia 'home' al nombre de tu vista de inicio
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'login.html')


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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Inicia sesión automáticamente al usuario después de registrarse
            login(request, user)
            return redirect('home')  # Cambia 'home' por la URL a la que quieras redirigir al usuario después de registrarse
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
