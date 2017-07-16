from django.contrib import admin

from django.contrib import admin
from album.models import (
		Category,
        SubCategory,
        ChildSubCategory,
        Gallery,
		Photos
	)


class ChildSubCategoryInline(admin.TabularInline):
    model = ChildSubCategory

class SubCategoryAdmin(admin.ModelAdmin):
    inlines = [
        ChildSubCategoryInline,
    ]

admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Category)
admin.site.register(Gallery)
admin.site.register(Photos)
