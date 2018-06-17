"""AgroTech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import logout,login
from django.urls import path, include
from rest_framework import routers

from AgroTech import settings
from core import views
from catalog.api.viewsets import ProductViewSet, CategoryViewSet
from catalog.models import Product, Category

router = routers.DefaultRouter()
router.register(r'produtos', ProductViewSet, base_name=Product)
router.register(r'categorias', CategoryViewSet, base_name=Category)


urlpatterns = [
    path('', views.home, name='home'),
    path('vendas/', views.index, name='index'),
    path('contato/', views.contact, name='contact'),
    path('entrar/', login, {'template_name': 'login.html'}, name='login'),
    path('sair/', logout, {'next_page': 'home'}, name='logout'),
    path('registro/', views.register, name='register'),
    path('catalogo/', include('catalog.urls', namespace="catalog")),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('conta/', include('accounts.urls', namespace='accounts')),
    path('compras/', include('checkout.urls', namespace='checkout')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('servicos/',include('servico_profissional.urls', namespace='profissional_servicos')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
