from django.shortcuts import render
from .models import CentroComercial, Tienda

# Create your views here.
def lista_centros_comerciales(request):
    centros_comerciales = CentroComercial.objects.all()
    return render(request, 'lista_centros_comerciales.html', {'centros_comerciales': centros_comerciales})

def lista_centros_tiendas(request):
    tiendas = Tienda.objects.all()
    return render(request, 'lista_tiendas.html', {'tiendas': tiendas})