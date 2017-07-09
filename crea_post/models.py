from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField
# from sortedm2m.fields import SortedManyToManyField
from .managers import GalleryQuerySet



class Photo(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    images = models.ImageField(upload_to='images/%Y', null=True)

    def __str__(self):
        return self.title


class Countries(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "countries"


MY_CHOICES = (('1', 'level 1'),
          ('2', 'level 2'),
          ('3', 'level 3'))


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    vprevia = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # images = models.ForeignKey('Photo', on_delete=models.CASCADE,null=True)
    post_level = models.CharField(max_length=1, choices=MY_CHOICES)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, null=True)
    text2 = MarkdownxField(null=True)
    
    def __str__(self):
        return self.title

    def publish(self):
        self.published_date= timezone.now()
        self.save()


class Categoria(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    photos = models.ManyToManyField(Photo, related_name="Foto")
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    objects = GalleryQuerySet.as_manager()

    def __str__(self):
        return self.title

class SubCategoria(models.Model):
    title = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    photos = models.ManyToManyField(Photo, related_name="subcategoryphoto", null=True)

    def __str__(self):
        return self.title