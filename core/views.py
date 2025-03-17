from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect
from .forms import VisitForm
from .models import Master, Service, Visit
from django.views.generic.edit import CreateView


MENU =[
    {'title': 'Главная', 'url': '/', 'active': True},
    {'title': 'Мастера', 'url': '/#masters/', 'active': True},
    {'title': 'Услуги', 'url': '/#services/', 'active': True},
    # {'title': 'Отзывы', 'url': '/#reviews/', 'active': True},
    # {'title': 'Оставить отзыв', 'url': '/reviews/create/', 'active': True},
    {'title': 'Запись на стрижку', 'url': '/#orderForm', 'active': True},
]

class ThanksView(TemplateView):
    template_name = 'thanks.html'
    extra_context = {'menu': MENU}

class IndexView(CreateView):
    tamplate_name = 'main.html'
    form_class = VisitForm
    success_url = 'thanks'
    model = Visit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MENU
        context['masters'] = Master.objects.all()
        context['services'] = Service.objects.all()
        return context