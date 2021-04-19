import os

from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver

# Estilo de Obra
class ScoreGenre(models.Model):
    
    name = models.CharField(max_length=200, 
        help_text="Ingrese el nombre del Estilo de Obra",
        verbose_name="Nombre")

    def __str__(self):

        return self.name

    class Meta:
        verbose_name = "Estilo de Obra"
        verbose_name_plural = "Estilos de Obra"
        

# Categoria de Partitura
class SheetCategory(models.Model):

    name = models.CharField(max_length=200,
        help_text="Ingrese el nombre de la Categoria de Partitura",
        verbose_name="Nombre")

    def __str__(self):

        return self.name

    class Meta:
        verbose_name = "Categoría de Partitura"
        verbose_name_plural = "Categorías de Partitura"

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

# Compositor
class Composer(models.Model):

    name = models.CharField(max_length=200,
        help_text="Ingrese el nombre del Compositor",
        verbose_name="Nombre")
    surname = models.CharField(max_length=200,
        help_text="Ingrese los apellidos del Compositor",
        verbose_name="Apellidos")
    web = models.CharField(max_length=200,
        help_text="Ingrese la web del Compositor",
        verbose_name="Web",
        null=True,
        blank=True)
    biography = models.TextField(max_length=1500,
        help_text="Ingrese la biografia del Compositor",
        verbose_name="Biografía",
        null=True,
        blank=True)
    photo = models.ImageField(upload_to="composers",
        help_text="Seleccione una imagen del Compositor",
        verbose_name="Fotografía",
        null=True,
        blank=True)

    def __str__(self):

        return '%s %s' % (self.name, self.surname)
    
    class Meta:
        verbose_name = "Compositor"
        verbose_name_plural = "Compositores"
# Eliminar la foto al borrar el compositor
@receiver(models.signals.post_delete, sender=Composer)
def auto_delete_photo_on_delete(sender, instance, **kwargs):
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)

# Eliminar foto antigua al modificar el compositor
@receiver(models.signals.pre_save, sender=Composer)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = Composer.objects.get(pk=instance.pk).photo
    except Composer.DoesNotExist:
        return False

    new_file = instance.photo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

# Video
class VideoMedia(models.Model):

    url = models.CharField(max_length=200,
        help_text="Ingrese la url de Youtube del vídeo")

    def __str__(self):

        return self.url
    
    class Meta:
        verbose_name = "Grabación de Vídeo"
        verbose_name_plural = "Grabaciones de Vídeo"

# Obra Musical
class Score(models.Model):

    tittle = models.CharField(max_length=200,
        help_text="Ingrese el titulo de la Obra",
        verbose_name="Título")
    composers = models.ManyToManyField(Composer,
        related_name='composed_scores',
        help_text="Seleccione los Compositores",
        verbose_name="Compositores")
    genre = models.ForeignKey(ScoreGenre,
        on_delete=models.CASCADE,
        help_text="Seleccione el Estilo",
        verbose_name="Estilo")
    registry = models.IntegerField(null=True,
        help_text="Introduzca la referencia en el Archivo",
        verbose_name="Archivo",
        blank=True)
    arrangers = models.ManyToManyField(Composer,
        related_name='arranged_scores',
        help_text="Seleccione los Arreglista",
        verbose_name="Arreglistas",
        blank=True)
    mp3 = models.FileField(upload_to="audio",
        null=True,
        blank=True)
    video = models.ManyToManyField(VideoMedia,
        related_name='scores',
        help_text="Seleccione el Vídeo",
        blank=True)

    def __str__(self):

        return '%s (%s)' % (self.tittle, self.genre)
    
    class Meta:
        verbose_name = "Obra Musical"
        verbose_name_plural = "Obras Musicales"


# Partitura
class Sheet(models.Model):

    pdf = models.FileField(upload_to="sheets")
    category = models.ForeignKey(SheetCategory,
        on_delete=models.CASCADE,
        help_text="Seleccione la Categoria",
        verbose_name="Categoría")
    score = models.ForeignKey(Score,
        on_delete=models.CASCADE,
        help_text="Seleccione la Obra Musical",
        verbose_name="Obra Musical")

    def __str__(self):

        return '%s (%s)' % (self.category, self.score)

    class Meta:
        verbose_name = "Partitura"
        verbose_name_plural = "Partituras"

# Eliminar el archivo al borrar la partitura
@receiver(models.signals.post_delete, sender=Sheet)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.pdf:
        if os.path.isfile(instance.pdf.path):
            os.remove(instance.pdf.path)

# Eliminar archivo antiguo al modificar la partitura
@receiver(models.signals.pre_save, sender=Sheet)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = Sheet.objects.get(pk=instance.pk).pdf
    except Sheet.DoesNotExist:
        return False

    new_file = instance.pdf
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

# Musico
class Musician(models.Model):

    user = models.OneToOneField(User,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="Usuario")
    ins = models.CharField(max_length=200,
        default='Clarinete',
        help_text="Ingrese el instrumento del musico",
        verbose_name="Instrumento")
    sheets = models.ManyToManyField(Sheet,
        related_name='musicians',
        help_text="Asigne partituras al musico",
        verbose_name="Partituras",
        blank=True)

    def __str__(self):
        if self.user.first_name:
            if self.user.last_name:
                return '%s %s' % (self.user.first_name, self.user.last_name)
            else:
                return '%s' % (self.user.first_name)
        else:
            return '%s' % (self.user.username)

    class Meta:
        verbose_name = "Músico"
        verbose_name_plural = "Músicos"


# Material
class Material(models.Model):

    INSTRUMENTO = 'I'
    UNIFORME = 'U'
    OTRO = 'O'

    CATEGORY_CHOICES = (
        (INSTRUMENTO,'Instrumento'),
        (UNIFORME,'Uniforme'),
        (OTRO,'Otro'),
    )
    name = models.CharField(max_length=200,
        help_text="Ingrese el nombre del Material",
        verbose_name="Nombre")
    category = models.CharField(max_length=1,
        choices=CATEGORY_CHOICES,
        default=OTRO,
        verbose_name="Categoría")
    musician = models.ForeignKey(Musician,
        null=True,
        on_delete=models.CASCADE,
        help_text="Seleccione un Musico",
        verbose_name="Músico",
        blank=True)

    def __str__(self):

        return '%s (%s)' % (self.name, self.category)

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"

# Evento
class Event(models.Model):

    ACTUACION = 'A'
    ENSAYO = 'E'

    CATEGORY_CHOICES = (
        (ACTUACION,'Actuacion'),
        (ENSAYO,'Ensayo'),
    )

    name = models.CharField(max_length=200,
        help_text="Ingrese el nombre del Evento",
        verbose_name="Nombre")
    place = models.CharField(max_length=200,
        help_text="Ingrese el lugar del Evento",
        verbose_name="Lugar")
    category = models.CharField(max_length=1,
        choices=CATEGORY_CHOICES,
        default=ACTUACION,
        verbose_name="Categoría")
    startDate = models.DateTimeField(verbose_name="Fecha de Inicio")
    endDate = models.DateTimeField(verbose_name="Fecha de Finalización")
    reward = models.DecimalField(decimal_places=2,
        max_digits=8,
        help_text="Introduzca la gratificacion",
        verbose_name="Gratificación",
        null=True,
        blank=True)
    scores = models.ManyToManyField(Score,
        related_name='events',
        help_text="Asigne obras al evento",
        verbose_name="Partituras",
        blank=True)
    musicians = models.ManyToManyField(Musician,
        related_name='events',
        help_text="Asigne musicos al evento",
        verbose_name="Músicos",
        blank=True)
    videos = models.ManyToManyField(VideoMedia,
        related_name='events',
        help_text="Añada vídeos del evento",
        verbose_name="Videos",
        blank=True)

    def __str__(self):

        return '%s (%s)' % (self.name, self.startDate)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
