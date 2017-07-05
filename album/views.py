from django.shortcuts import render
from album.models import Category, Photo
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView


#def first_view(request):
#    return HttpResponse('Esta es mi primera vista')
#
#
#def category(request):
#    category_list = Category.objects.all()
#    context = {'object_list': category_list}
#    return render(request, 'album/category_list.html', context)
#
#
#def category_detail(request, category_id):
#    category = Category.objects.get(id=category_id)
#    context = {'object': category}
#    return render(request, 'album/category_detail.html', context)


def base(request):
    return render(request, 'base1.html')


class CategoryListView(ListView):
    model = Category
    #template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        # q = Photo.objects.get(pk=1)
        context['photo'] = Photo.objects.first()
        return context


class CategoryDetailView(DetailView):
    model = Category


class PhotoListView(ListView):
    model = Photo


class PhotoDetailView(DetailView):
    model = Photo


class PhotoUpdate(UpdateView):
    model = Photo


class PhotoCreate(CreateView):
    model = Photo


class PhotoDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('photo-list')