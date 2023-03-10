from .models import Image
from .serializers import BasicImageSerializer, PremiumImageSerializer
from rest_framework import generics


class ImageView(generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Image.objects.filter(owner=self.request.user)

    def get_serializer_class(self):
        if self.request.user.groups:
            return PremiumImageSerializer
        return BasicImageSerializer