from rest_framework import serializers
from .models import Image
from easy_thumbnails_rest.serializers import ThumbnailerListSerializer

# class ImageSerializer(serializers.Serializer):
#     owner = serializers.ReadOnlyField(source='user.username')
#     image = serializers.


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    thumbnail = serializers.ImageField()

    class Meta:
        model = Image
        fields = ('owner', 'thumbnail')