from django.db import models
from django.contrib.auth.models import User
# Estilo de Obra
class ScoreGenre(models.Model):
    
    name = models.CharField(max_length=200, help_text="Ingrese el nombre del Estilo de Obra")

    def __str__(self):

        return self.name

# Categoria de Partitura
class SheetCategory(models.Model):

    name = models.CharField(max_length=200, help_text="Ingrese el nombre de la Categoria de Partitura")

    def __str__(self):

        return self.name

# Libro de Cuentas
class Ledger(models.Model):

    name = models.CharField(max_length=200, help_text="Ingrese el nombre del Libro de Cuentas")
    initialBalance = models.DecimalField(decimal_places=2, max_digits=8, help_text="Ingrese el saldo inicial")
    currentBalance = models.DecimalField(decimal_places=2,max_digits=8)

    def __str__(self):

        return self.name

# Ejercicio
class Period(models.Model):

    name = models.CharField(max_length=200, help_text="Ingrese el nombre del Ejercicio")
    initialBalance = models.DecimalField(decimal_places=2,max_digits=8, help_text="Ingrese el saldo inicial")
    currentBalance = models.DecimalField(decimal_places=2, max_digits=8)
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE, help_text="Seleccione el Libro de Cuentas")

    def __str__(self):

        return '%s (%s)' % (self.name, self.ledger.name)

# Entrada
class Entry(models.Model):

    date = models.DateField(auto_now=True)
    concept = models.CharField(max_length=200, help_text="Ingrese el concepto")
    initialBalance = models.DecimalField(decimal_places=2, max_digits=8)
    endBalance = models.DecimalField(decimal_places=2, max_digits=8)
    amount = models.DecimalField(decimal_places=2, max_digits=8, help_text="Introduzca la cantidad")
    spendig = models.BooleanField(help_text="Marque la casilla si se trata de un gasto")
    period = models.ForeignKey(Period, on_delete=models.CASCADE, help_text="Seleccione el Ejercicio")

    def __str__(self):

        return '%s (%s)' % (self.date, self.period.name)

# Compositor
class Composer(models.Model):

    name = models.CharField(max_length=200, help_text="Ingrese el nombre del Compositor")
    surname = models.CharField(max_length=200, help_text="Ingrese los apellidos del Compositor")
    web = models.CharField(max_length=200, help_text="Ingrese la web del Compositor")
    biography = models.CharField(max_length=1500, help_text="Ingrese la biografia del Compositor")
    photo = models.ImageField(help_text="Seleccione una imagen del Compositor")

    def __str__(self):

        return '%s (%s)' % (self.name, self.surname)

# Video
class Video(models.Model):

    url = models.CharField(max_length=200, help_text="Ingrese el titulo de la Obra")

    def __str__(self):

        return self.url

# Obra Musical
class Score(models.Model):

    tittle = models.CharField(max_length=200, help_text="Ingrese el titulo de la Obra")
    composers = models.ManyToManyField(Composer, related_name='composed_scores', help_text="Seleccione el Compositor")
    genre = models.ForeignKey(ScoreGenre,on_delete=models.CASCADE, help_text="Seleccione el Estilo")
    registry = models.IntegerField(null=True, help_text="Introduzca la referencia en el Archivo")
    arrangers = models.ManyToManyField(Composer, related_name='arranged_scores', help_text="Seleccione el Arreglista")
    mp3 = models.FileField(null=True)
    video = models.ManyToManyField(Video,related_name='scores', help_text="Seleccione el Estilo")

    def __str__(self):

        return '%s (%s)' % (self.tittle, self.genre)


# Partitura
class Sheet(models.Model):

    pdf = models.FileField()
    category = models.ForeignKey(SheetCategory, on_delete=models.CASCADE, help_text="Seleccione la Categoria")
    score = models.ForeignKey(Score, on_delete=models.CASCADE, help_text="Seleccione la Obra Musical")

    def __str__(self):

        return '%s (%s)' % (self.pdf, self.score.tittle)
    
# Musico
class Musician(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    ins = models.CharField(max_length=200,default='Clarinete', help_text="Ingrese el instrumento del musico")
    sheets = models.ManyToManyField(Sheet, related_name='musicians', help_text="Asigne partituras al musico")

    def __str__(self):

        return self.user


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
    name = models.CharField(max_length=200, help_text="Ingrese el nombre del Material")
    category = models.CharField(max_length=1,choices=CATEGORY_CHOICES,default=OTRO)
    musician = models.ForeignKey(Musician, null=True, on_delete=models.CASCADE, help_text="Seleccione un Musico")

    def __str__(self):

        return '%s (%s)' % (self.name, self.category)

# Evento
class Event(models.Model):

    ACTUACION = 'A'
    ENSAYO = 'E'

    CATEGORY_CHOICES = (
        (ACTUACION,'Actuacion'),
        (ENSAYO,'Ensayo'),
    )

    name = models.CharField(max_length=200, help_text="Ingrese el nombre del Evento")
    place = models.CharField(max_length=200, help_text="Ingrese el lugar del Evento")
    category = models.CharField(max_length=1,choices=CATEGORY_CHOICES,default=ACTUACION)
    startDate = models.DateField()
    endDate = models.DateField()
    reward = models.DecimalField(decimal_places=2, max_digits=8, help_text="Introduzca la gratificacion")
    scores = models.ManyToManyField(Score, related_name='events', help_text="Asigne obras al evento")
    musicians = models.ManyToManyField(Musician, related_name='events', help_text="Asigne musicos al evento")
    videos = models.ManyToManyField(Video,related_name='events', help_text="Seleccione el Estilo")

    def __str__(self):

        return '%s (%s)' % (self.name, self.startDate)