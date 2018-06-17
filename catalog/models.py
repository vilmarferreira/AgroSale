from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    name=models.CharField('Nome', max_length=100)
    slug= models.SlugField('Identificador', max_length=100)

    created= models.DateTimeField('Criado em', auto_now_add=True) #setar a data atual quando é criado
    modified = models.DateTimeField('Modificado em', auto_now=True) #para setar a data de modificação da categoria
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering=['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:category', kwargs={'slug':self.slug})


class Product (models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    category = models.ForeignKey(Category, verbose_name='Categoria',on_delete=models.CASCADE)   #Chave estrangeiro
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=10) # define 2 casas decimais e no máximo 10 digitos para o preço do produto
    image = models.ImageField(upload_to='imag_product', null=True,
                              blank=True)  # Configuração de imagem para realizar o upload
    created = models.DateTimeField('Criado em', auto_now_add=True)  # setar a data atual quando é criado
    modified = models.DateTimeField('Modificado em', auto_now=True)  # para setar a data de modificação da categoria

    class Meta:
        verbose_name= 'Produto'
        verbose_name_plural ='Produtos'
        ordering=['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product',kwargs={'slug':self.slug})