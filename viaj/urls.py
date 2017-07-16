"""viaj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from viaj.views import home_page, nosotros, galeria, contacto, colabora
from crea_post.views import viaje, post_ver, countryView, categoryView, subCategoryView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name= "inicio"),
    url(r'^inicio/$', home_page, name= "inicio"),
    url(r'^nosotros/$', nosotros, name= "nosotros"),
    url(r'^viaje/$', viaje, name= "viaje"),
    url(r'^country/(?P<pk>[0-9]+)/$', countryView, name= "country"),
    url(r'^category/(?P<pk>[0-9]+)/$', categoryView, name= "category"),
    url(r'^subcategory/(?P<pk>[0-9]+)/$', subCategoryView, name= "sub_category"),
    url(r'^post_ver/(?P<pk>[0-9]+)/$', post_ver, name= "post_ver"),
    # url(r'^galeria/$', galeria, name= "galeria"),
    url(r'^contacto/$', contacto, name= "contacto"),
    url(r'^colabora/$', colabora, name= "colabora"),
    # url(r'^tinymce/', include('tinymce.urls')),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^album/', include('album.urls'), name= "album"),
    # url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

]

if  settings.DEBUG:
    urlpatterns	+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)