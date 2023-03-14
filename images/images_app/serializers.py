from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    thumbnails = serializers.ListField(child=serializers.ImageField(read_only=True), read_only=True)
    original_image = serializers.ImageField(read_only=True)
    image = serializers.ImageField(write_only=True)

    class Meta:
        model = Image
        fields = ['owner', 'original_image', 'thumbnails', 'image']
