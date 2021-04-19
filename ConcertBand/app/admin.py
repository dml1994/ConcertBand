from django.contrib import admin
from .models import *
from django.utils.translation import ngettext
from django.contrib import messages


# Libro de Cuentas
class LedgerAdmin(admin.ModelAdmin):
    list_display = ('name','initialBalance','currentBalance')
    exclude = ('currentBalance',)
    actions = ['delete_ledgers']

    @admin.action(description="Elimina los libros de cuentas seleccionados")
    def delete_ledgers(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, ngettext(
            'El Libro de Cuentas ha sido eliminado con éxito',
            'Los Libros de Cuentas han sido eliminados con éxito',
            queryset,
            ), messages.SUCCESS)

# Ejercicio
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('name','initialBalance','currentBalance','ledger')
    exclude = ('initialBalance','currentBalance')
    actions = ['delete_periods']

    @admin.action(description="Elimina los ejercicios seleccionados")
    def delete_periods(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, ngettext(
            'El Ejercicio ha sido eliminado con éxito',
            'Los Ejercicios han sido eliminados con éxito',
            queryset,
            ), messages.SUCCESS)

# Entrada
class EntryAdmin(admin.ModelAdmin):
    list_display = ('concept','amount','date','initialBalance','endBalance','period')
    exclude = ('initialBalance','endBalance')
    actions = ['delete_entries']
    search_fields = ('concept',)
    date_hierarchy = 'date'
    fields = ('concept',('amount','spending'),'period')

    @admin.action(description="Elimina las entradas seleccionadas")
    def delete_entries(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, ngettext(
            'La Entrada ha sido eliminada con éxito',
            'Las Entradas han sido eliminadas con éxito',
            queryset,
            ), messages.SUCCESS)

# Categoria de Partitura
class SheetCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    actions = ['delete_sheets']
    search_fields = ('name',)

    @admin.action(description="Elimina las categorías seleccionadas")
    def delete_sheets(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, ngettext(
            'La Categoría ha sido eliminada con éxito',
            'Las Categorías han sido eliminadas con éxito',
            queryset,
            ), messages.SUCCESS)

# Estilos de Obra
class ScoreGenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    actions = ['delete_genres']
    search_fields = ('name',)

    @admin.action(description="Elimina los estilos seleccionados")
    def delete_genres(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, ngettext(
            'El Estilo ha sido eliminado con éxito',
            'Los Estilos han sido eliminados con éxito',
            queryset,
            ), messages.SUCCESS)

# Compositor
class ComposerAdmin(admin.ModelAdmin):
    list_display = ('name','surname')
    actions = ['delete_composers']
    search_fields = ('name','surname')

    @admin.action(description="Elimina los compositores seleccionados")
    def delete_composers(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, ngettext(
            'El Compositor ha sido eliminado con éxito',
            'Los Compositores han sido eliminados con éxito',
            queryset,
            ), messages.SUCCESS)

# Video
class VideoMediaAdmin(admin.ModelAdmin):
    list_display = ('url',)
    actions = ['delete_videos']
    search_fields = ('url',)

    @admin.action(description="Elimina los vídeos seleccionados")
    def delete_videos(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, ngettext(
            'El vídeo ha sido eliminado con éxito',
            'Los Vídeos han sido eliminados con éxito',
            queryset,
            ), messages.SUCCESS)

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

# Partitura
class SheetAdmin(admin.ModelAdmin):
    list_display = ('category','score')
    actions = ['delete_sheets']
    search_fields = ('category','score')
    list_filter = ('category',)

    @admin.action(description="Elimina las partituras seleccionadas")
    def delete_sheets(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, ngettext(
            'La Partitura ha sido eliminada con éxito',
            'Las Partituras han sido eliminados con éxito',
            queryset,
            ), messages.SUCCESS)

# Obra Musical
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('tittle','genre','registry')
    actions = ['delete_scores']
    search_fields = ('tittle',)
    list_filter = ('genre','composers')

    @admin.action(description="Elimina las obras seleccionadas")
    def delete_scores(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, ngettext(
            'La Obra ha sido eliminada con éxito',
            'Las Obras han sido eliminados con éxito',
            queryset,
            ), messages.SUCCESS)


admin.site.register(ScoreGenre, ScoreGenreAdmin)
admin.site.register(SheetCategory, SheetCategoryAdmin)
admin.site.register(Ledger, LedgerAdmin)
admin.site.register(Period, PeriodAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Composer, ComposerAdmin)
admin.site.register(VideoMedia,VideoMediaAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Sheet, SheetAdmin)
admin.site.register(Musician, MusicianAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Event, EventAdmin)

admin.site.disable_action('delete_selected')
