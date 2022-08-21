from django.shortcuts import render
from django.contrib.messages import constants
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url= '/auth/logar')
def home(request):
        messages.add_message(request, constants.DEBUG, 'Seja Bem-Vindo')
        return render(request, 'plataforma.html')
