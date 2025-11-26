from django.urls import path

from .views import *


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
]