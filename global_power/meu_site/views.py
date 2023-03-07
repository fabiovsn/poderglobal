from django.shortcuts import render
from django.http import HttpResponse
from api.models import PoderGlobal

# Create your views here.

def index(request):
    Pais1 = None
    Pais2 = None

    Paises = PoderGlobal.objects.all()

    busca1 = request.GET.get('search1')
    busca2 = request.GET.get('search2')

    if busca1:
        Pais1 = PoderGlobal.objects.filter(nome_pais__icontains=busca1)

    if busca2:
        Pais2 = PoderGlobal.objects.filter(nome_pais__icontains=busca2)

    return render(request, 'index.html', {'Paises': Paises, 'Pais1': Pais1, 'Pais2': Pais2})

def quemsou(request):
    return render(request, 'quemsou.html')