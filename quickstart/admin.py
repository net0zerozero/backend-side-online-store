from django.contrib import admin
from .models import Category, Product, UserData

admin.site.register(UserData)

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('title',)

    def __str__(self) -> str:
        return self.title


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('title',)

    def __str__(self) -> str:
        return self.title
