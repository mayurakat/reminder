from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RemindMeLaterSerializer
from .models import RemindMeLater


# Create your views here.
class RemindMeLaterViewset(viewsets.ModelViewSet):
    serializer_class = RemindMeLaterSerializer
    queryset = RemindMeLater.objects.all().order_by('id')
    permission_classes = []
