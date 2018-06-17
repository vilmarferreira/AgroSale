# coding=utf-8

from django import forms
from django.core.mail import  send_mail
from django.conf import settings


class ContactForm(forms.Form):

    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())


    ####controlando como renderizar ####
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['class'] = 'form-control'


    ##metodo para enviar email###
    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        mensagem = self.cleaned_data['message']
        mensagem = 'Nome:{0}\nE-mail: {1}\nMensagem: {2}'.format(name, email, mensagem)
        send_mail('Contado do ecommerce', mensagem, settings.DEFAULT_FROM_EMAIL,
                  [settings.DEFAULT_FROM_EMAIL]
                  )
