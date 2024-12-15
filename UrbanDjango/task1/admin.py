from django.contrib import admin
from .models import *


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size', 'description', 'age_limited')
    list_filter = ('size', 'cost')
    search_fields = ('title', )  # поле для поиска
    list_per_page = 20  # Количество объекто вдля отображения на странице


@admin.register(Buyer)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    list_filter = ('balance', 'age')
    search_fields = ('name', )  # поле для поиска
    list_per_page = 30  # Количество объекто вдля отображения на странице

    readonly_fields = ('balance',)


@admin.register(News)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date')
    list_filter = ('date', )
    search_fields = ('title', )  # поле для поиска
    list_per_page = 20  # Количество объекто вдля отображения на странице
