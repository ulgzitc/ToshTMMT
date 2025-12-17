from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Elonlar, Yangiliklar, Yunalishlar, Rahbariyat, Haqimizda

class StaticSitemap(Sitemap):
    def items(self):
        return ['homepage', 'elonlar', 'yangiliklar', 'tarix', 'yunalishlar', 'rahbariyat', 'hamkorlik']

    def location(self, item):
        return reverse(item)


class HaqimizdaSitemap(Sitemap):
    def items(self):
        return Haqimizda.objects.all()
        

class RahbariyatSitemap(Sitemap):
    def items(self):
        return Rahbariyat.objects.all()


class YunalishlarSitemap(Sitemap):
    def items(self):
        return Yunalishlar.objects.all()


class YangiliklarSitemap(Sitemap):
    def items(self):
        return Yangiliklar.objects.all()


class ElonlarSitemap(Sitemap):
    def items(self):
        return Elonlar.objects.all()
        