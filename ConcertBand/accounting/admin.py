from django.contrib import admin
from .models import Ledger, Entry, Period
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



admin.site.register(Ledger, LedgerAdmin)
admin.site.register(Period, PeriodAdmin)
admin.site.register(Entry, EntryAdmin)

