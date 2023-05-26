from django.contrib import admin

from foodgram.settings import CONST_NUMBER_ONE

from .models import Favourite, Ingredient, Recipe, ShoppingCart, Tag


class IngredientRecipeInLine(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = CONST_NUMBER_ONE


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('measurement_unit', 'name')
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name', 'measurement_unit')
    empty_value_display = '-пусто-'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    list_editable = ('slug',)
    search_fields = ('slug',)
    list_filter = ('slug', 'name')
    empty_value_display = '-пусто-'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'cooking_time', 'text', 'name')
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name', 'cooking_time')
    empty_value_display = '-пусто-'
    inlines = (IngredientRecipeInLine, )


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user')
    list_editable = ('user',)
    search_fields = ('user',)
    list_filter = ('user', 'recipe')
    empty_value_display = '-пусто-'


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user')
    list_editable = ('user',)
    search_fields = ('user',)
    list_filter = ('user', 'recipe')
    empty_value_display = '-пусто-'
