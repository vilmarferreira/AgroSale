from django.db import models

# Create your models here.
from django.urls import reverse


class CategoryService(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    def get_absolute_url(self):
        return reverse('catalog:product',kwargs={'slug':self.slug})
class experienciaProfissional(models.Model):
    local = models.CharField(max_length=150)
    periodo = models.CharField(max_length=150)
    descricao= models.TextField(blank=True,null=True)

class PerfilProfissional(models.Model):
    #user = models.CharField(max_length=100, default=User.)
    nomeCompleto= models.CharField(max_length=100)
    foto = models.ImageField(upload_to='img_perfil')
    dataNascimento = models.DateField()
    profissao = models.CharField(max_length=100)
    experiencias = models.ManyToManyField(experienciaProfissional)
    categoria = models.ForeignKey(CategoryService,on_delete=models.CASCADE)
    def __str__(self):
        return self.nomeCompleto

    def get_absolute_url(self):
        return reverse('catalog:product',kwargs={'slug':self.slug})