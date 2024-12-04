# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = AuthenticationForm()

    return render(request, 'usuarios_login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso! Agora, você pode fazer o login.")
            return redirect('login')  # Redireciona para a página de login
        else:
            messages.error(request, "Erro ao criar conta. Tente novamente.")
    else:
        form = UserCreationForm()

    return render(request, 'usuarios_register.html', {'form': form})


