from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Colaborador

# Create your views here.
# ALG: Após a definicao das view é necessaria a criacao das rotas no arquivo urls.py no projeto principal
# ALG: Cada view retorna um template HTML diferente. Que deve ser criado na pasta templates definida no settings.py
def index(request):
    contexto = {
        'nome_site': 'Meu Site Django',
        'descricao': 'Bem-vindo ao meu site criado com Django!'
    }
    return render(request, 'index.html', contexto)

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def colaborador(request):
    colaboradores = Colaborador.objects.all()
    contexto = {
        'titulo': 'Colaboradores',
        'info': 'Lista de Colaboradores',
        'descricao': 'Conheça os colaboradores do nosso projeto.',
        'colaboradores': colaboradores
    }
    return render(request, 'colaborador.html', contexto)

def perfil(request, id):
    # Recupera o colaborador pelo ID
    #data = Colaborador.objects.get(id=id)

    # Usando get_object_or_404 para retornar 404 se o colaborador não for encontrado
    data = get_object_or_404(Colaborador, id=id)

    print(f'ID do colaborador: {id} - Nome: {data.nome} - Email: {data.email} - Telefone: {data.telefone}')
    contexto = {
        'colaborador': data
    }
    return render(request, 'perfil.html', contexto)

def custom_404_view(request, exception):
    template = loader.get_template('errors/404.html')
    return HttpResponse(content=template.render({}, request), content_type='text/html; charset=utf-8', status=404)

def custom_500_view(request):
    template = loader.get_template('errors/500.html')
    return HttpResponse(content=template.render({}, request), content_type='text/html; charset=utf-8', status=500)