from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Subscribe, UserFoodgram

admin.site.unregister(Group)


@admin.register(UserFoodgram)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name')
    list_editable = ('username',)
    search_fields = ('username',)
    list_filter = ('username',)
    empty_value_display = '-пусто-'


@admin.register(Subscribe)
class SubscribeUserAdmin(admin.ModelAdmin):
    list_display = ('author', 'user')
    list_editable = ('user',)
    search_fields = ('user',)
    list_filter = ('user',)
    empty_value_display = '-пусто-'
