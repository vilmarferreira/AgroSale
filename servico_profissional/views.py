from django.shortcuts import render
from .models import PerfilProfissional
# Create your views here.


def ViewCurriculo(request):
    return  render(request, 'servico_profissional/Curriculo.html')

def ViewServicos(request):
    list = PerfilProfissional.objects.all()
    context ={
        'list': list
    }
    return render(request,'servico_profissional/Serviços.html', context)