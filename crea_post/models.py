from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField
# from sortedm2m.fields import SortedManyToManyField
from .managers import GalleryQuerySet



class Photo(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    images = models.ImageField(upload_to='posts/%Y', null=True)

    def __str__(self):
        return self.title


MY_CHOICES = (('1', 'level 1'),
          ('2', 'level 2'),
          ('3', 'level 3'))


class Countries(models.Model):
    name = models.CharField(max_length=80)
    has_category = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "countries"

class Categoria(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    has_sub_category = models.BooleanField(default=False)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, null=True)
    # photos = models.ManyToManyField(Photo, related_name="Foto", null=True)

    objects = GalleryQuerySet.as_manager()

    def __str__(self):
        return self.title

class SubCategoria(models.Model):
    title = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    # photos = models.ManyToManyField(Photo, related_name="subcategoryphoto", null=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    vprevia = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # images = models.ForeignKey('Photo', on_delete=models.CASCADE,null=True)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)
    sub_categoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE, blank=True, null=True)
    text2 = MarkdownxField(null=True)
    
    def __str__(self):
        return self.title

    def publish(self):
        self.published_date= timezone.now()
        self.save()