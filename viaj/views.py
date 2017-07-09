from django.shortcuts import render

from django.template import RequestContext
from django.utils import timezone

from crea_post.models import Post

def home_page(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:5]
	return render(request,'index.html',{'posts': posts})

def nosotros(request):
	return render(request,'nosotros.html',{})

def galeria(request):
	return render(request,'galeria.html',{})

def contacto(request):
	return render(request,'contacto.html',{})

def colabora(request):
	return render(request,'colabora.html',{})
