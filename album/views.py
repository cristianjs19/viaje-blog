from django.shortcuts import render, get_object_or_404
from album.models import Category, Photos, Gallery, SubCategory, ChildSubCategory
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


def CategoryListView(request):
    categorySet = Category.objects.all()
    context = {
        'categorySet': categorySet
    }
    return render(request,'album/category.html', context)


def subCategoryView(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if category.has_category:
        subCategorySet = SubCategory.objects.filter(category=category)

        context = {
            'subCategorySet': subCategorySet
        }
        return render(request,'album/subcategory.html',context)
    else:
        gallerySet = Gallery.objects.filter(category=category)
        galleryData = []
        for gallery in gallerySet:
            lastPhoto = Photos.objects.filter(gallery=gallery).order_by('-id')
            galleryData.append({
                    'gallery_id':gallery.id,
                    'lastPhoto': lastPhoto[0].photo.url if lastPhoto else None,
                    'title': gallery.title
                })

        context = {
            'gallerySet': galleryData
        }
        return render(request,'album/gallery.html',context)



def ChildSubCategoryView(request, pk):
    subCategory = get_object_or_404(SubCategory, pk=pk)

    if subCategory.has_category:
        childSubCategorySet = ChildSubCategory.objects.filter(sub_category=subCategory)

        context = {
            'childSubCategorySet': childSubCategorySet
        }
        return render(request,'album/childsubcategory.html',context)
    else:
        gallerySet = Gallery.objects.filter(sub_category=subCategory)
        galleryData = []
        for gallery in gallerySet:
            lastPhoto = Photos.objects.filter(gallery=gallery).order_by('-id')
            galleryData.append({
                    'gallery_id':gallery.id,
                    'lastPhoto': lastPhoto[0].photo.url if lastPhoto else None,
                    'title': gallery.title
                })

        context = {
            'gallerySet': galleryData
        }
        return render(request,'album/gallery.html',context)

def galleryView(request, pk):
    childSubCategory = get_object_or_404(ChildSubCategory, pk=pk)

    gallerySet = Gallery.objects.filter(child_sub_category=childSubCategory)
    galleryData = []
    for gallery in gallerySet:
        lastPhoto = Photos.objects.filter(gallery=gallery).order_by('-id')
        galleryData.append({
                'gallery_id':gallery.id,
                'lastPhoto': lastPhoto[0].photo.url if lastPhoto else None,
                'title': gallery.title
            })

    context = {
        'gallerySet': galleryData
    }
    return render(request,'album/gallery.html',context)


def galleryDetailView(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)

    photoSet = Photos.objects.filter(gallery=gallery)

    context = {
        'photoSet': photoSet
    }

    return render(request,'album/photos.html', context)

# class PhotoDetailView(DetailView):
#     model = Photos


# class PhotoUpdate(UpdateView):
#     model = Photos


# class PhotoCreate(CreateView):
#     model = Photos


# class PhotoDelete(DeleteView):
#     model = Photos
#     success_url = reverse_lazy('photo-list')