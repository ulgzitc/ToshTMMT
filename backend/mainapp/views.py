from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Elonlar, Yangiliklar
from .serializers import ElonlarSerializer, YangiliklarSerializer


class ElonlarView(generics.ListAPIView):
    queryset = Elonlar.objects.all()
    serializer_class = ElonlarSerializer

class ElonView(generics.RetrieveAPIView):
    queryset = Elonlar.objects.all()
    serializer_class = ElonlarSerializer
    lookup_field = 'slug'

class YangiliklarView(generics.ListAPIView):
    queryset = Yangiliklar.objects.all()
    serializer_class = YangiliklarSerializer


class YangilikView(generics.RetrieveAPIView):
    queryset = Yangiliklar.objects.all()
    serializer_class = YangiliklarSerializer
    lookup_field = 'slug'