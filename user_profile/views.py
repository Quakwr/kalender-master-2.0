from django.shortcuts import render, redirect
from .models import Gasto
from .forms import NuevoGasto

# Create your views here.

def NuevoGastoView(request):
	return render(request, 'acceso.html')

def subirgasto(request):
	if request.method=="POST":
		form = NuevoGasto(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return redirect('acceso')
	else:
		form=NuevoGasto()
	return render(request, 'nuevogasto.html',{
        'form':form
		})

def vergasto(request):
	lista_gastos= Gasto.objects.all()
	return render(request, 'vergastos.html', {
        'lista_gastos': lista_gastos
    })

def verlink(request, pk):
    enlace = Gasto.objects.get(pk=pk)
    return render(request, 'verlink.html', {
        'enlace':enlace
    })

def borrarlink(request, pk):
    if request.method == "POST":
        borrar = Gasto.objects.get(pk=pk)
        borrar.delete()
    return redirect('vergastos')
	
def calendario(request, año, mes):
	nombre = {{user.username}}
	return render(request, 'mainpage.html', {'nombre' : nombre })