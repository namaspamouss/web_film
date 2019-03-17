from django.http import Http404
from django.shortcuts import render, get_object_or_404
from blog.models import Article, Contact
from .forms import ContactForm, ArticleForm, NouveauContactForm

def accueil(request):
    articles = Article.objects.all()
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})

def lire(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/lire.html', {'article': article})

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']
        envoi = True
    return render(request, 'blog/contact.html', locals())

def creer_article(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        envoi = True
    return render(request, 'blog/creer.html', locals())

def nouveau_contact(request):
    sauvegarde = False
    form = NouveauContactForm(request.POST or None, request.FILES)
    if form.is_valid():
        contact = Contact()
        contact.nom = form.cleaned_data["nom"]
        contact.adresse = form.cleaned_data["adresse"]
        contact.photo = form.cleaned_data["photo"]
        contact.save()
        sauvegarde = True

    return render(request, 'blog/creer_contact.html', {
        'form': form,
        'sauvegarde': sauvegarde
    })

def voir_contacts(request):
    return render(request, 'blog/voir_contacts.html', {'contacts': Contact.objects.all()})


