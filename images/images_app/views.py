from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Image
from .serializers import ImageSerializer
from rest_framework import generics
from rest_framework import permissions


class ImageView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# class ImageView(APIView):
#     def get(self, request):
#         images = [image.image.thumbnails.small.url for image in Image.objects.all()]
#         return Response(images)