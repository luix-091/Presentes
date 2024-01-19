from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from PIL import Image
from .forms import PresenteForm
from .models import Presente

def logar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Usuário não encontrado!')

        user = authenticate(request, username=username, password=senha)
        print(user)
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

def cadastro_desejo(request):
    if request.method == 'POST':
        form = PresenteForm(request.POST)
        if form.is_valid():
            presente = form.save(commit=False)
            presente.usuario = request.user
            print(request.FILES.get('foto').name)
            presente.foto = request.FILES.get('foto')
            presente.save()
            return redirect('home')
    else:
        form = PresenteForm()

    return render(request, 'templates/cadastro-desejo.html', {'form': form})

def meus_desejos(request):
    presentes = Presente.objects.all()
    conteudo = {'presentes': presentes}
    return render(request, 'templates/meus-desejos.html', conteudo)

def apagar_presente(request, presente_id):
    presente = get_object_or_404(Presente, id=presente_id)
    
    if request.method == 'POST':
        presente.delete()
    
    return redirect('meus-desejos')