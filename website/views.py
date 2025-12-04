from django.shortcuts import render

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

