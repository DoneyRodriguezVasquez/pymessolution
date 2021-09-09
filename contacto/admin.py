from django.contrib import admin
from .models import Contactos


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email','nombre','telefono','mensaje', 'contactos_recientes', 'fecha')
    list_filter = ('fecha',)
    search_fields = ('email','nombre','fecha')
admin.site.register(Contactos, ContactAdmin)
