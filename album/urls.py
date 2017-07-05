from django.conf.urls import url
from album import views


urlpatterns = (
                       url(r'^$', views.base, name='base1'),
                       url(r'^category/$', views.CategoryListView.as_view(), name='category-list'),
                       url(r'^category/(?P<pk>\d+)/detail/$', views.CategoryDetailView.as_view(),
                           name='category-detail'),
                       url(r'^photo/$', views.PhotoListView.as_view(), name='photo-list'),
                       url(r'^photo/(?P<pk>\d+)/detail/$', views.PhotoDetailView.as_view(),
                           name='photo-detail'),
                       # Update
                       url(r'^photo/(?P<pk>\d+)/update/$', views.PhotoUpdate.as_view(), name='photo-update'),
                       #Create
                       url(r'^photo/create/$', views.PhotoCreate.as_view(), name='photo-create'),
                       #Delete
                       url(r'^photo/(?P<pk>\d+)/delete/$', views.PhotoDelete.as_view(), name='photo-delete'),
                       )