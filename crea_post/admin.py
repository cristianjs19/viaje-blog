from django.contrib import admin
from django.db import models
from .models import Post, Categoria, Photo
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget
from markdownx.models import MarkdownxField

# class PostAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.TextField: {'widget': AdminMarkdownxWidget},
#         markdownx.models.MarkdownxField: {'widget': AdminMarkdownxWidget},
#     }

# admin.site.register(Post, PostAdmin, )
admin.site.register(Post,MarkdownxModelAdmin,)
admin.site.register(Categoria,)
admin.site.register(Photo,)
