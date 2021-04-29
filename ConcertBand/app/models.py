import os

from django.db import models
from django.contrib.auth.models import User
from registry.models import Sheet,Score,VideoMedia
from django.dispatch import receiver
       

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
