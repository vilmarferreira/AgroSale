from django.shortcuts import render
from .models import PerfilProfissional
# Create your views here.


def ViewCurriculo(request, id):
    perfil = PerfilProfissional.objects.get(pk=id)
    context = {
        'perfil':perfil
    }
    return  render(request, 'servico_profissional/Curriculo.html', context)

def ViewServicos(request):
    list = PerfilProfissional.objects.all()
    context ={
        'list': list
    }
    return render(request,'servico_profissional/Serviços.html', context)