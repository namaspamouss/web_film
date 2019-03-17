from django.urls import path
from blog import views

urlpatterns = [
    path('', views.accueil, name = 'index_blog'),
    path('article/<int:id>-<slug:slug>', views.lire, name = 'lire'),
    path('contact/', views.contact, name='contact'),
    path('creer/', views.creer_article, name = 'creer'),
    path('creer_contact/', views.nouveau_contact, name = 'creer_contact'),
    path('voir_contacts/', views.voir_contacts, name = 'voir_contacts'),
]