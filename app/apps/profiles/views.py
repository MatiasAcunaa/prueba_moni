from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def signupp(request):
    from django.contrib.auth.models import User
    if request.method == 'GET':
        return render(request, 'signupp.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                username = request.POST['username']
                # Verifico si el nombre de usuario ya existe
                if User.objects.filter(username=username).exists():
                    return render(request, 'signupp.html', {
                        'form': UserCreationForm,
                        'error': 'El usuario ya existe'
                    })
                # Si el nombre de usuario no existe, creo un nuevo usuario
                user = User.objects.create_user(username=username, password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('loans')
            except IntegrityError:
                return render(request, 'signupp.html', {
                    'form': UserCreationForm,
                    'error': 'Ocurrió un error al crear el usuario'
                })
        return render(request, 'signupp.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
        'form' : AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form' : AuthenticationForm,
                'error' : 'El usuario o la constrasena son incorectos'
            })
        else:
            login(request, user)
            return redirect('loans')