from django.db import models

# Libro de Cuentas
class Ledger(models.Model):

    name = models.CharField(max_length=200,
        help_text="Ingrese el nombre del Libro de Cuentas",
        verbose_name="Nombre")
    initialBalance = models.DecimalField(decimal_places=2,
        max_digits=8,
        help_text="Ingrese el saldo inicial",
        verbose_name="Saldo inicial")
    currentBalance = models.DecimalField(decimal_places=2,
        max_digits=8,
        verbose_name="Saldo actual",
        null=True)

    def __str__(self):

        return self.name
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.currentBalance = self.initialBalance
        super().save(*args,**kwargs)

    class Meta:
        verbose_name = "Libro de Cuentas"
        verbose_name_plural = "Libros de Cuentas"
        ordering = ("name",)

# Ejercicio
class Period(models.Model):

    name = models.CharField(max_length=200,
        help_text="Ingrese el nombre del Ejercicio",
        verbose_name="Nombre")
    initialBalance = models.DecimalField(decimal_places=2,
        max_digits=8,
        help_text="Ingrese el saldo inicial",
        verbose_name="Saldo inicial",
        null=True)
    currentBalance = models.DecimalField(decimal_places=2,
        max_digits=8,
        verbose_name="Saldo Actual",
        null=True)
    ledger = models.ForeignKey(Ledger,
        on_delete=models.CASCADE,
        help_text="Seleccione el Libro de Cuentas",
        verbose_name="Libro de Cuentas")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.initialBalance = self.ledger.currentBalance
            self.currentBalance = self.ledger.currentBalance
        super().save(*args,**kwargs)

    def __str__(self):

        return '%s (%s)' % (self.name, self.ledger.name)

    class Meta:
        verbose_name = "Ejercicio"
        verbose_name_plural = "Ejercicios"
        ordering = ("ledger","name")

# Entrada
class Entry(models.Model):

    date = models.DateTimeField(auto_now=True,
        verbose_name="Fecha")
    concept = models.CharField(max_length=200,
        help_text="Ingrese el concepto",
        verbose_name="Concepto")
    initialBalance = models.DecimalField(decimal_places=2,
        max_digits=8,
        verbose_name="Saldo inicial",
        null=True)
    endBalance = models.DecimalField(decimal_places=2,
        max_digits=8,
        verbose_name="Saldo final",
        null=True)
    amount = models.DecimalField(decimal_places=2,
        max_digits=8,
        help_text="Introduzca la cantidad",
        verbose_name="Cantidad")
    spending = models.BooleanField(help_text="Marque la casilla si se trata de un gasto",
        verbose_name="Gasto")
    period = models.ForeignKey(Period,
        on_delete=models.CASCADE,
        help_text="Seleccione el Ejercicio",
        verbose_name="Ejercicio")

    def __str__(self):

        return '%s (%s)' % (self.date, self.period.name)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.initialBalance = self.period.currentBalance
            if self.spending:
                self.endBalance = self.period.currentBalance - self.amount
            else:
                self.endBalance = self.period.currentBalance + self.amount
            self.period.currentBalance = self.endBalance
            self.period.ledger.currentBalance = self.endBalance
            self.period.save()
            self.period.ledger.save()
        super().save(*args,**kwargs)

    def delete(self, *args, **kwargs):
        if self.spending:
            self.period.currentBalance = self.period.currentBalance + self.amount
            self.period.ledger.currentBalance = self.period.ledger.currentBalance + self.amount
        else:
            self.period.currentBalance = self.period.currentBalance - self.amount
            self.period.ledger.currentBalance = self.period.ledger.currentBalance - self.amount
        self.period.save()
        self.period.ledger.save()
        super(Entry,self).delete(*args, **kwargs)
    
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ("period", "date")

