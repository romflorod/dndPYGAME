from django.contrib import admin
from .models import Draconido, Elfo, Enano, Gnomo, Humano, Mediano, Semielfo, Semiorco, Tiefling
@admin.register(Draconido)
class DraconidoAdmin(admin.ModelAdmin):
    pass

@admin.register(Elfo)
class ElfoAdmin(admin.ModelAdmin):
    pass

@admin.register(Enano)
class EnanoAdmin(admin.ModelAdmin):
    pass

@admin.register(Gnomo)
class GnomoAdmin(admin.ModelAdmin):
    pass

@admin.register(Humano)
class HumanoAdmin(admin.ModelAdmin):
    pass

@admin.register(Mediano)
class MedianoAdmin(admin.ModelAdmin):
    pass

@admin.register(Semielfo)
class SemielfoAdmin(admin.ModelAdmin):
    pass

@admin.register(Semiorco)
class SemiorcoAdmin(admin.ModelAdmin):
    pass

@admin.register(Tiefling)
class TieflingAdmin(admin.ModelAdmin):
    pass
