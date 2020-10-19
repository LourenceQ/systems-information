from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'si_app/index.html')

def algo(request):
    return render(request,'si_app/algo.html')

def arq(request):
    return render(request,'si_app/arquitetura.html')

def ing(request):
    return render(request,'si_app/ingles.html')

def proj(request):
    return render(request,'si_app/projetos.html')

def moni(request):
    return render(request,'si_app/monitoria.html')

def quemsou(request):
    return render(request,'si_app/quemsou.html')
