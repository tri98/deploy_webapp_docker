from django import forms
from .models import Wordpress

class WordpressForm(forms.ModelForm):
    class Meta:
        model = Wordpress
        fields = ('containerWordpress', 'wordpressUser', 'wordpressPassword', 'containerSql', 'sqlUser', 'sqlPassword', 'sqlRootPassword')