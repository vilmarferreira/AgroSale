from django.shortcuts import render

# Create your views here.


def ViewCurriculo(request):
    return  render(request, 'servico_profissional/Curriculo.html')

def ViewServicos(request):
    return render(request,'servico_profissional/Serviços.html')