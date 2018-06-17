from django.urls import path
from . import views
app_name = 'servicoes_profissional'

urlpatterns = [
    path('', views.ViewServicos, name='listProfissional'),
]