from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

# Register

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registro exitoso." )
			return redirect("homepage")
		messages.error(request, "Error en el registro, revisa la información entregada.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

# Login

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Bienvenido, {username}.")
				return redirect("acceso")
			else:
				messages.error(request,"Usuario o contraseña inválidos.")
		else:
			messages.error(request,"Usuario o contraseña inválidos.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("homepage")

def mainpage_request(request):
    return render(request, "mainpage.html")
def acceso_request(request):
    return render(request, "acceso.html")