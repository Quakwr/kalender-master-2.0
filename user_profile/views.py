from django.shortcuts import render, redirect
from .models import Gasto, calendario
from .forms import NuevoGasto, lista, actualizarform

# Create your views here.

def NuevoGastoView(request):
	return render(request, 'vergastos.html')

def subirgasto(request):
	if request.method=="POST":
		form = NuevoGasto(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return redirect('vergastos')
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
	
def kalendar(request):
	queryset = calendario.objects.order_by('hecho','fecha')
	form = lista()
	if request.method =='POST':
		form = lista(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/calendario/')
	context = {
		'tasks':queryset,
		'form':form,
		}
	return render(request, 'calendario.html', context)

def actualizar_calendario(request, pk):
	queryset = calendario.objects.get(id=pk)
	form = actualizarform(instance=queryset)
	if request.method == 'POST':
		form = actualizarform(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/calendario/')

	context = {
		'form':form
		}

	return render(request, 'update_task.html', context)

def borrarfecha(request, pk):
	queryset = calendario.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/calendario/')

	context = {
		'item':queryset
		}
	return render(request, 'borrar_fecha.html', context)