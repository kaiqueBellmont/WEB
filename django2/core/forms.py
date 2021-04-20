from django import forms
from datetime import datetime


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    data = forms.DateField(label='Data', initial=datetime.today)
    if data.initial != datetime.today:
        data.initial = datetime.today()

    assunto = forms.CharField(label="Assunto", max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())
