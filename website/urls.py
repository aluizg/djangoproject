from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('colaborador/', views.colaborador, name='colaborador'),
    path('perfil/<int:id>', views.perfil, name='perfil'),
]