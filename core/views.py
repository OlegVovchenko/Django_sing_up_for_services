from django.views.generic import TemplateView

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = MENU
        return context