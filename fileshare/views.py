from rest_framework import generics, permissions
from .models import File
from .serializers import FileSerializer

class FileList(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]