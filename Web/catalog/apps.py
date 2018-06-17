from django.apps import AppConfig
from watson import search as watson

class CatologConfig(AppConfig):
    name = 'catalog'
    verbose_name='Catálogo'

    def ready(self):
        Product = self.get_model('Product')
        watson.register(Product)

