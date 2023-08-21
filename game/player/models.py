from django.db import models

class Draconido(models.Model):
    nombre = models.CharField(max_length=100)
    velocidad = models.PositiveIntegerField(default=30)
    linaje_draconico = models.CharField(max_length=100, blank=True)
    ataque_de_aliento = models.CharField(max_length=100, blank=True)
    resistencia_al_danio = models.CharField(max_length=100, blank=True)
    idiomas = models.CharField(max_length=100, default="Común, Dragón")
    fuerza_mod = models.IntegerField(default=2)
    carisma_mod = models.IntegerField(default=1)
    edad = models.PositiveIntegerField(default=500)

class Elfo(models.Model):
    nombre = models.CharField(max_length=100)
    velocidad = models.PositiveIntegerField(default=30)
    vision_en_la_oscuridad = models.BooleanField(default=True)
    linaje_feerico = models.BooleanField(default=True)
    trance = models.BooleanField(default=True)
    idiomas = models.CharField(max_length=100, default="Común, Élfico")
    destreza_mod = models.IntegerField(default=2)
    edad = models.PositiveIntegerField(default=500)

class Enano(models.Model):
    nombre = models.CharField(max_length=100)
    velocidad = models.PositiveIntegerField(default=25)
    vision_en_la_oscuridad = models.BooleanField(default=True)
    fortaleza_enana = models.BooleanField(default=True)
    afinidad_con_la_piedra = models.BooleanField(default=True)
    idiomas = models.CharField(max_length=100, default="Común, Enano")
    constitucion_mod = models.IntegerField(default=2)
    herramientas_de_artesano = models.CharField(max_length=100, blank=True)
    edad = models.PositiveIntegerField(default=500)

class Gnomo(models.Model):
    nombre = models.CharField(max_length=100)
    velocidad = models.PositiveIntegerField(default=25)
    vision_en_la_oscuridad = models.BooleanField(default=True)
    astucia_de_gnomo = models.BooleanField(default=True)
    idiomas = models.CharField(max_length=100, default="Común, Gnomo")
    inteligencia_mod = models.IntegerField(default=2)
    edad = models.PositiveIntegerField(default=500)

class Humano(models.Model):
    nombre = models.CharField(max_length=100)
    velocidad = models.PositiveIntegerField(default=30)
    alineamiento = models.CharField(max_length=100, default="Varía ampliamente")
    idiomas = models.CharField(max_length=100, default="Común y un idioma adicional de elección")
    fuerza_mod = models.IntegerField(default=1)
    destreza_mod = models.IntegerField(default=1)
    constitucion_mod = models.IntegerField(default=1)
    inteligencia_mod = models.IntegerField(default=1)
    sabiduria_mod = models.IntegerField(default=1)
    carisma_mod = models.IntegerField(default=1)
    edad = models.PositiveIntegerField(default=100)

class Mediano(models.Model):
    nombre = models.CharField(max_length=100)
    velocidad = models.PositiveIntegerField(default=25)
    idiomas = models.CharField(max_length=100, default="Común, Mediano")
    agilidad_de_los_medianos = models.BooleanField(default=True)
    valiente = models.BooleanField(default=True)
    afortunado = models.BooleanField(default=True)
    destreza_mod = models.IntegerField(default=2)
    edad = models.PositiveIntegerField(default=500)

class Semielfo(models.Model):
    nombre = models.CharField(max_length=100)
    velocidad = models.PositiveIntegerField(default=30)
    vision_en_la_oscuridad = models.BooleanField(default=True)
    ancestro_feerico = models.BooleanField(default=True)
    idiomas = models.CharField(max_length=100, default="Común, Élfico y un idioma adicional de elección")
    carisma_mod = models.IntegerField(default=2)
    mod_a_eleccion = models.IntegerField(default=1)
    edad = models.PositiveIntegerField(default=500)

class Semiorco(models.Model):
    nombre = models.CharField(max_length=100)
    velocidad = models.PositiveIntegerField(default=30)
    vision_en_la_oscuridad = models.BooleanField(default=True)
    aguante_incansable = models.BooleanField(default=True)
    ataques_salvajes = models.BooleanField(default=True)
    idiomas = models.CharField(max_length=100, default="Común, Orco")
    fuerza_mod = models.IntegerField(default=2)
    constitucion_mod = models.IntegerField(default=1)
    edad = models.PositiveIntegerField(default=500)

class Tiefling(models.Model):
    nombre = models.CharField(max_length=100)
    velocidad = models.PositiveIntegerField(default=30)
    vision_en_la_oscuridad = models.BooleanField(default=True)
    legado_infernal = models.BooleanField(default=True)
    resistencia_infernal = models.BooleanField(default=True)
    idiomas = models.CharField(max_length=100, default="Común, Infernal")
    carisma_mod = models.IntegerField(default=2)
    inteligencia_mod = models.IntegerField(default=1)
    edad = models.PositiveIntegerField(default=500)
