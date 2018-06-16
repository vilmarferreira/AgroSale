from django.conf.urls import url
from django.urls import path

from . import views

app_name="catalog"
urlpatterns=[

    path('',views.product_list, name='product_list'),
    url(r'^(?P<slug>[\w-]+)/$', views.category, name='category'),
    url(r'^produtos/(?P<slug>[\w-]+)/$', views.product, name='product'),
]