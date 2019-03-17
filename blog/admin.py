from django.contrib import admin
from django.utils.text import Truncator
# Register your models here.

from blog.models import Categorie, Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date', 'apercu_contenu')
    list_filter = ('auteur', 'categorie',)
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('titre', 'contenu')

    fieldsets = (
        ('Général', {
            'classes': ['collapse',],
            'fields': ('titre', 'auteur', 'categorie', 'slug')
        }),
        ('contenu de l\'article', {
            'description': 'ce formulaire accepte les balises HTML',
            'fields': ('contenu', )    
        }),
    )

    def apercu_contenu(self, article):
        return Truncator(article.contenu).chars(40, truncate='...')

    apercu_contenu.short_description = 'Aperçu de contenu'
    

admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
