from django.contrib import admin
from .models import *
from django.utils.translation import ngettext
from django.contrib import messages



class LedgerAdmin(admin.ModelAdmin):
    list_display = ('name','initialBalance','currentBalance')
    exclude = ('currentBalance',)
    actions = ['delete_selected']

class PeriodAdmin(admin.ModelAdmin):
    list_display = ('name','initialBalance','currentBalance','ledger')
    exclude = ('initialBalance','currentBalance')
    actions = ['delete_selected']


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


admin.site.register(ScoreGenre)
admin.site.register(SheetCategory)
admin.site.register(Ledger, LedgerAdmin)
admin.site.register(Period, PeriodAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Composer)
admin.site.register(Video)
admin.site.register(Score)
admin.site.register(Sheet)
admin.site.register(Musician)
admin.site.register(Material)
admin.site.register(Event)

admin.site.disable_action('delete_selected')