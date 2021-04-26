from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Contato
from .forms import ContatoForm
from django.views.generic import FormView, CreateView


class IndexView(SuccessMessageMixin, CreateView):
    model = Contato
    fields = ['nome', 'telefone', 'email', 'mensagem']
    template_name = 'index.html'
    success_url = reverse_lazy('index')
    success_message = 'Deu certo!'

    def form_valid(self, form):
        form.save()
        return super(IndexView, self).form_valid(form)
