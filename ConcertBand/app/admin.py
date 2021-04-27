from django.contrib import admin
from .models import *
from django.utils.translation import ngettext
from django.contrib import messages




# Eventos
class EventAdmin(admin.ModelAdmin):
    list_display = ('name','place','category','startDate','endDate')
    actions = ['delete_events']
    search_fields = ('name','place')

    @admin.action(description="Elimina los eventos seleccionados")
    def delete_events(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, ngettext(
            'El Evento ha sido eliminado con éxito',
            'Los Eventos han sido eliminados con éxito',
            queryset,
            ), messages.SUCCESS)

# Material
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name','category','musician')
    actions = ['delete_materials']
    search_fields = ('name','category','musician')
    list_filter = ('category',)

    @admin.action(description="Elimina los materiales seleccionados")
    def delete_materials(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, ngettext(
            'El Material ha sido eliminado con éxito',
            'Los Materiales han sido eliminados con éxito',
            queryset,
            ), messages.SUCCESS)

# Musico
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('user','ins')
    actions = ['delete_musicians']
    search_fields = ('user','inst')
    list_filter = ('ins',)

    @admin.action(description="Elimina los músicos seleccionados")
    def delete_musicians(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, ngettext(
            'El Músico ha sido eliminado con éxito',
            'Los Músicos han sido eliminados con éxito',
            queryset,
            ), messages.SUCCESS)




admin.site.register(Musician, MusicianAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Event, EventAdmin)

admin.site.disable_action('delete_selected')
