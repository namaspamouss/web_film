from django import forms
from .models import Article, Contact

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé", required=False) 

    def clean_message(self):
        message = self.cleaned_data['message']
        if "pizza" in message:
            raise forms.ValidationError("on ne veut pas entendre parler de pizza !")

        return message


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class NouveauContactForm(forms.Form):
    nom = forms.CharField()
    adresse = forms.CharField(widget = forms.Textarea)
    photo = forms.ImageField()