from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def viaje(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'viaje.html',{'posts': posts})

def post_ver(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request,'post_ver.html',{'post': post})
