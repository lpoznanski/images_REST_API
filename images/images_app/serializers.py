from rest_framework import serializers
from models import Image

class ImageSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Image
        fields = ('image', 'user')