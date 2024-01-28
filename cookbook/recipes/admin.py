from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product, Recipe, RecipeProduct


class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct
    min_num = 1
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'count']
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ('name',)
    empty_value_display = '-пусто-'
    inlines = (RecipeProductInline,)


@admin.register(RecipeProduct)
class RecipeProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'recipe', 'product', 'amount']
    search_fields = ('recipe', 'product')
    empty_value_display = '-пусто-'


admin.site.unregister(Group)
