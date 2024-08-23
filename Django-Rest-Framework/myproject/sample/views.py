from django.http import HttpResponse
from rest_framework import viewsets
from .models import URL
from .serializers import URLSerializer

def home(request):
    return HttpResponse("Welcome to the Home Page!")

class URLViewSet(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = URLSerializer
