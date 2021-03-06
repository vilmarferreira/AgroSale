# coding=utf-8
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import  send_mail
from django.urls import reverse_lazy

from .forms import ContactForm
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth import get_user_model

class HomeView(TemplateView):
    template_name = 'home.html'

home = HomeView.as_view()
class IndexView(TemplateView):


    template_name = 'index.html'


index = IndexView.as_view()

def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success= True

    context = {
        'form': form,
        'success':success
    }
    return render(request, 'contact.html', context)

class RegisterView(CreateView):

    form_class = UserCreationForm
    template_name = 'register.html'
    model = User
    success_url = reverse_lazy('index')


register = RegisterView.as_view()

