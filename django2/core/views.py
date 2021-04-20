from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        print(f'POST: {request.POST}')
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            data = form.cleaned_data['data']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print(f'Mensagem enviada')
            print(f'nome : {nome}')
            print(f'email: {email}')
            print(f'Data: {data}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')

            messages.success(request, 'Mensagem enviada com Sucesso')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar mensagem')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    return render(request, 'produto.html')

