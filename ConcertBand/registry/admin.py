from django.contrib import admin
from .models import *
from django.utils.translation import ngettext
from django.contrib import messages

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

admin.site.register(ScoreGenre, ScoreGenreAdmin)
admin.site.register(SheetCategory, SheetCategoryAdmin)
admin.site.register(Composer, ComposerAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Sheet, SheetAdmin)
admin.site.register(VideoMedia,VideoMediaAdmin)

