from rest_framework import serializers
from .models import Elonlar, Yangiliklar

class ElonlarSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='elon',
        lookup_field = 'slug',
    )

    class Meta:
        model = Elonlar
        fields = '__all__'


class YangiliklarSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='yangilik',
        lookup_field = 'slug',
    )

    class Meta:
        model = Yangiliklar
        fields = '__all__'
