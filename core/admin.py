from django.contrib import admin
from .models import People


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_display_links = ('name', 'address')
    search_fields = ('name', 'address')
    list_per_page = 10

admin.site.register(People, PeopleAdmin)
