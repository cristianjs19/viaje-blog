from django.conf.urls import url
from album import views


urlpatterns = (
                       url(r'^$', views.base, name='base1'),
                       url(r'^category/$', views.CategoryListView, name='category-list'),
                       url(r'^category/(?P<pk>\d+)/$', views.subCategoryView,
                           name='category-detail'),
                       url(r'^subcategory/(?P<pk>\d+)/$', views.ChildSubCategoryView,
                           name='subcategory'),
                       url(r'^childsubcategory/(?P<pk>\d+)/$', views.galleryView,
                           name='subcategory'),
                       # url(r'^photo/$', views.PhotoListView.as_view(), name='photo-list'),
                       url(r'^gallery/(?P<pk>\d+)/detail/$', views.galleryDetailView,
                           name='photo-detail'),
                       # # Update
                       # url(r'^photo/(?P<pk>\d+)/update/$', views.PhotoUpdate.as_view(), name='photo-update'),
                       # #Create
                       # url(r'^photo/create/$', views.PhotoCreate.as_view(), name='photo-create'),
                       # #Delete
                       # url(r'^photo/(?P<pk>\d+)/delete/$', views.PhotoDelete.as_view(), name='photo-delete'),
                       )