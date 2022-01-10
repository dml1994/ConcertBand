import os

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

# Video
class VideoMedia(models.Model):

    title = models.CharField(max_length=200, 
        help_text="Ingrese el título del vídeo",
        verbose_name="Título",
        null=True)
    url = models.CharField(max_length=200,
        help_text="Ingrese la url de Youtube del vídeo")

    def __str__(self):

        return self.title
    
    class Meta:
        verbose_name = "Grabación de Vídeo"
        verbose_name_plural = "Grabaciones de Vídeo"
        
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
    photo = models.FileField(upload_to="composers_photo",
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

