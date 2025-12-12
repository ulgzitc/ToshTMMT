from django.views.generic import ListView, DetailView, TemplateView
from django.views import View
from django.core.paginator import Paginator

from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

from .models import Elonlar, Yangiliklar, Yunalishlar, Rahbariyat, Haqimizda


class HomepageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['elonlar'] = Elonlar.objects.order_by("-date")[:3]
        context['yangiliklar'] = Yangiliklar.objects.order_by("-date")[:4]
        return context
    



############ Elon
class ElonlarView(ListView):
    model = Elonlar
    template_name = 'annauncements.html'
    context_object_name = 'objects'
    paginate_by = 6
    ordering = ['-date']

class ElonView(DetailView):
    model = Elonlar
    template_name = 'annauncement.html'
    context_object_name = 'object'

############ Yanglik
class YangiliklarView(ListView):
    model = Yangiliklar
    template_name = 'news.html'
    context_object_name = 'objects'
    paginate_by = 6
    ordering = ['-date']

class YangilikView(DetailView):
    model = Yangiliklar
    template_name = 'new.html'
    context_object_name = 'object'



class YunalishView(ListView):
    model = Yunalishlar
    context_object_name = 'objects'
    template_name = 'branches.html'
    
    

class TarixView(ListView):
    model = Haqimizda
    context_object_name = 'objects'
    template_name = 'haqida.html'

class RaxbariyatView(ListView):
    model = Rahbariyat
    template_name = 'rahbariyat.html'
    context_object_name = 'objects'


class HamkorlikView(TemplateView):
    template_name = 'hamkorlik.html'
