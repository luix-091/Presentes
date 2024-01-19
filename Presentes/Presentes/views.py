from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def logar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Usuário não encontrado!')

        user = authenticate(request, username=username, password=senha)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha não foram encontrados!')

    return render(request, 'templates/login.html')

def deslogar(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'templates/home.html')