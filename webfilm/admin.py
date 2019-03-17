from django.contrib import admin

# Register your models here.
from webfilm.models import Roles, Acteurs, Films

class FilmAdmin(admin.ModelAdmin):
    list_display = ('titre','realisateur','affiche','annee')
    ordering = ('-annee', )
    search_fields = ('titre', 'realisateur')
    
    fieldsets = (
        ('film', {
            "fields": ('titre','realisateur','affiche','annee'),
        }),
    )

admin.site.register(Roles)
admin.site.register(Acteurs)
admin.site.register(Films, FilmAdmin)
