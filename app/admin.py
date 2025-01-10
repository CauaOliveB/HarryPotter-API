from django.contrib import admin
from .models import *

# Register your models here.

class datSpell(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10
    
admin.site.register(Spell, datSpell)

class datHouse(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 10
    
admin.site.register(House, datHouse)

class datChar(admin.ModelAdmin):
    list_display = ('id', 'name', 'wizard', 'house', 'species', 'ancestry', 'eyeColor', 'hairColor', 'actor')
    list_display_links = ('id', 'name',)
    list_per_page = 10
    
admin.site.register(Characters, datChar)


