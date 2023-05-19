from django.contrib import admin
from .models import Category, Product, UserData


class UserDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('is_admin', 'is_active', 'is_superuser', 'date_joined')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')

    def __str__(self) -> str:
        return self.title


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at', 'category')

    def __str__(self) -> str:
        return self.title


admin.site.register(UserData, UserDataAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
