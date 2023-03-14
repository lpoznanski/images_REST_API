from .models import Image
from .serializers import ImageSerializer
from rest_framework import generics


class ImageView(generics.ListCreateAPIView):
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Image.objects.filter(owner=self.request.user)
