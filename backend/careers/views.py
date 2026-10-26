from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from .models import Career
from .serializers import CareerSerializer

class CareerListView(generics.ListAPIView):
    queryset = Career.objects.all().order_by("title")
    serializer_class = CareerSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ["title", "sector", "description"]

class CareerDetailView(generics.RetrieveAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    permission_classes = [permissions.AllowAny]
