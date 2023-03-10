from rest_framework import serializers
from .models import Image


class BasicImageSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    small = serializers.ImageField(read_only=True)
    image = serializers.ImageField(write_only=True)

    class Meta:
        model = Image
        fields = ('owner', 'small', 'image')


class PremiumImageSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    small = serializers.ImageField(read_only=True)
    large = serializers.ImageField(read_only=True)

    class Meta:
        model = Image
        fields = ('owner', 'small', 'large', 'image')