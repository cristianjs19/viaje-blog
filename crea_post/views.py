from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Categoria, SubCategoria, Countries

def viaje(request):
	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	countrySet = Countries.objects.all()
	return render(request,'viaje.html',{'countrySet': countrySet})	

def post_ver(request, pk):
	post = get_object_or_404(Post, pk=pk)

	context = {
		'post': post
	}
	return render(request,'posts_details.html',context)



def countryView(request, pk):
	country = get_object_or_404(Countries, pk=pk)

	if country.has_category:
		categorySet = Categoria.objects.filter(country=country)

		context = {
			'categorySet': categorySet
		}
		return render(request,'categories.html',context)
	else:
		postSet = Post.objects.filter(country=country)
		context = {
			'postSet': postSet
		}
		return render(request,'posts.html',context)


def categoryView(request, pk):
	categoria = get_object_or_404(Categoria, pk=pk)

	if categoria.has_sub_category:
		subCategoriaSet = SubCategoria.objects.filter(categoria=categoria)

		context = {
			'subCategoriaSet': subCategoriaSet
		}
		return render(request,'subcategories.html',context)
	else:
		postSet = Post.objects.filter(categoria=categoria)
		context = {
			'postSet': postSet
		}
		return render(request,'posts.html',context)


def subCategoryView(request, pk):
	subCategoria = get_object_or_404(SubCategoria, pk=pk)

	postSet = Post.objects.filter(sub_categoria=subCategoria)
	context = {
		'postSet': postSet
	}
	return render(request,'posts.html',context)