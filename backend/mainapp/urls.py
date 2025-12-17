from django.urls import path
from django.contrib.sitemaps.views import sitemap

from .views import *
from .sitemaps import *

sitemaps = {
    'static' : StaticSitemap,
    'haqimizda' : HaqimizdaSitemap,
    'rahbariyat' : RahbariyatSitemap,
    'yunalishlar' : YunalishlarSitemap,
    'yangiliklar' : YangiliklarSitemap,
    'elonlar' : ElonlarSitemap
}


urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('elonlar/', ElonlarView.as_view(), name='elonlar'),
    path('yangiliklar/', YangiliklarView.as_view(), name='yangiliklar'),
    path('elonlar/<slug:slug>/', ElonView.as_view(), name='elon'),
    path('yangiliklar/<slug:slug>/', YangilikView.as_view(), name='yangilik'),
    path('tarix/', TarixView.as_view(), name='tarix'),
    path('yo`nalishlar/', YunalishView.as_view(), name='yunalishlar'),
    path('rahbariyat/', RaxbariyatView.as_view(), name='rahbariyat'),
    path('hamkorlik/', HamkorlikView.as_view(), name='hamkorlik'),
    path('sitemap.xml/', sitemap, {'sitemaps' : sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
]