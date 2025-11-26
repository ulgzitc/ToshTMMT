from django.views.generic import ListView, DetailView, TemplateView
from django.views import View

from .models import Elonlar, Yangiliklar


class HomepageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['elonlar'] = Elonlar.objects.order_by("-date")[:5]
        context['yangiliklar'] = Yangiliklar.objects.order_by("-date")[:5]
        return context
    
    



############ Elon
class ElonlarView(ListView):
    model = Elonlar
    template_name = ''
    context_object_name = 'elonlar'
    paginate_by = 5
    ordering = ['-date']

class ElonView(DetailView):
    model = Elonlar
    template_name = ''
    context_object_name = 'elon'

############ Yanglik
class YangiliklarView(ListView):
    model = Yangiliklar
    template_name = ''
    context_object_name = 'yangiliklar'
    paginate_by = 5
    ordering = ['-date']

class YangilikView(DetailView):
    model = Yangiliklar
    template_name = ''
    context_object_name = 'yangilik'



############ Qo`shimcha
class TarixView(TemplateView):
    template_name = ''

class YunalishView(TemplateView):
    template_name = ''

class RaxbariyatView(TemplateView):
    template_name = ''

class HamkorlikView(TemplateView):
    template_name = ''