from django.urls import path

from .views import *


urlpatterns = [
    path('elonlar/', ElonlarView.as_view(), name='elonlar'),
    path('yangiliklar/', YangiliklarView.as_view(), name='yangiliklar'),
    path('elonlar/<slug:slug>/', ElonView.as_view(), name='elon'),
    path('yangiliklar/<slug:slug>/', YangilikView.as_view(), name='yangilik'),
]