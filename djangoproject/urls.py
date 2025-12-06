"""
URL configuration for djangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# ALG: Importacao do modulo include para incluir as rotas do app website
# from  website.views import index, sobre, contato
# ALG: Melhor pratica manda importar include e criar um arquivo urls.py dentro do app

# ALG: Importacao do handler404 para customizar a pagina de erro 404
from django.conf.urls import handler404, handler500
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # ALG: Para qualquer requisicao a partir da raiz '', sera redirecionada para o arquivo urls.py do app website
    path('', include('website.urls')),

]

# ALG: Definicao do handler404 para customizar a pagina de erro 404
handler404 = views.custom_404_view
handler500 = views.custom_500_view