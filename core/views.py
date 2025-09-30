from django.shortcuts import render
from rest_framework import viewsets
from .models import Portfolio
from .serializers import PortfolioSerializer
# Create your views here


class PortfolioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Portfolio.objects.all().order_by('-created_at')
    serializer_class = PortfolioSerializer

