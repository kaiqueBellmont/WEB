from django import forms
from .models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'telefone', 'email', 'mensagem']

    def salvar(self):
        nome = self.cleaned_data['nome']
        telefone = self.cleaned_data['telefone']
        email = self.cleaned_data['telefone']
        mensagem = self.cleaned_data['mensagem']

        ContatoForm(nome, telefone, email, mensagem).save()
