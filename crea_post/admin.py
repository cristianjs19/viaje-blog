from django.contrib import admin
from django.db import models
from .models import (
	SubCategoria,
	Categoria,
	Countries,
	Photo,
	Post
	)
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget
from markdownx.models import MarkdownxField

# class PostAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.TextField: {'widget': AdminMarkdownxWidget},
#         markdownx.models.MarkdownxField: {'widget': AdminMarkdownxWidget},
#     }

# admin.site.register(Post, PostAdmin, )

# class PhotoInline(admin.StackedInline):
#     model = Photo
#     can_delete = False
#     verbose_name_plural = 'employee'

class SubCategoriaInline(admin.TabularInline):
    model = SubCategoria

class CategoriaAdmin(admin.ModelAdmin):
    inlines = [
        SubCategoriaInline,
    ]

# class CategoriaInline(admin.TabularInline):
#     model = Categoria

# class PostAdmin(admin.ModelAdmin):
# 	list_display = ('title', 'author', 'country', 'published_date')
# 	inlines = [
# 		CategoriaInline
# 	]


admin.site.register(Post, MarkdownxModelAdmin)     # (Post,PostAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Photo)
admin.site.register(Countries)
# admin.site.register(SubCategoria)
