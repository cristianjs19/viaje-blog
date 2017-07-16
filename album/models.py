from django.db import models
from django.db.models.signals import post_delete
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.utils import timezone



class Category(models.Model):
    name = models.CharField(max_length=50)
    has_category = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class SubCategory(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    has_category = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class ChildSubCategory(models.Model):
    title = models.CharField(max_length=200)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Gallery(models.Model):     # i changed the name "Photo" to "gallery" 
    """ Fotos del album """
    title = models.CharField(max_length=50, default='No title')
    pub_date = models.DateField(auto_now_add=True)
    favorite = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    child_sub_category = models.ForeignKey(ChildSubCategory, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo-list')


class Photos(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='album_photos/')

    class Meta:
        db_table = "album_photos"


# @receiver(post_delete, sender=Photo)
# def photo_delete(sender, instance, **kwargs):
#     """ Borra los ficheros de las fotos que se eliminan. """
#     instance.photo.delete(False)