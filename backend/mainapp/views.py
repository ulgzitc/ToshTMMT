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
    template_name = 'yangiliklar.html'
    context_object_name = 'objects'
    paginate_by = 2
    ordering = ['-date']

class ElonView(DetailView):
    model = Elonlar
    template_name = 'yangilik.html'
    context_object_name = 'object'

############ Yanglik
class YangiliklarView(ListView):
    model = Yangiliklar
    template_name = 'yangiliklar.html'
    context_object_name = 'objects'
    paginate_by = 2
    ordering = ['-date']

class YangilikView(DetailView):
    model = Yangiliklar
    template_name = 'yangilik.html'
    context_object_name = 'object'



############ Qo`shimcha
class TarixView(TemplateView):
    template_name = 'tarix.html'

class YunalishView(TemplateView):
    template_name = 'yonalishlar.html'

class RaxbariyatView(TemplateView):
    template_name = 'rahbariyat.html'

class HamkorlikView(TemplateView):
    template_name = 'hamkorlik.html'

class BoglanishView(TemplateView):
    template_name = 'boglanish'

class HaqidaView(TemplateView):
    template_name = 'haqida.html'