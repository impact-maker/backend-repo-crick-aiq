from .models import *
from .serializers import *
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters


class PredictionFilter(filters.FilterSet):
    class Meta:
        model = Prediction
        fields = {
            'format': ['exact'],
            'match_date': ['exact'],
            'status': ['exact']
        }

class PredictionViewSet(viewsets.ModelViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer
    filterset_class = PredictionFilter
    filter_backends = [rest_framework_filters.SearchFilter, filters.DjangoFilterBackend, rest_framework_filters.OrderingFilter]
    ordering_fields = ['created_on']
    ordering = ['-created_on']



class AnalysisFilter(filters.FilterSet):
    class Meta:
        model = Analysis
        fields = {
            'type': ['exact']
        }

class AnalysisViewSet(viewsets.ModelViewSet):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer
    filterset_class = AnalysisFilter
    filter_backends = [rest_framework_filters.SearchFilter, filters.DjangoFilterBackend, rest_framework_filters.OrderingFilter]
    ordering_fields = ['created_on']
    ordering = ['-created_on']