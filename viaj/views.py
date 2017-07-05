from django.shortcuts import render
from django.template import RequestContext

def home_page(request):
	return render(request,'index.html',{})

def nosotros(request):
	return render(request,'nosotros.html',{})

def galeria(request):
	return render(request,'galeria.html',{})

def contacto(request):
	return render(request,'contacto.html',{})

def colabora(request):
	return render(request,'colabora.html',{})
