from django.db import models
from django.urls import reverse_lazy


class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Contato(Base):
    nome = models.CharField('nome', max_length=100)
    telefone = models.CharField('telefone', max_length=15)
    email = models.EmailField('email', max_length=100)
    mensagem = models.CharField('mensagem', max_length=500)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse_lazy('index')
