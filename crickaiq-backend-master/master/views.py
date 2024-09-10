from .models import *
from .serializers import *
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters

class CountryFilter(filters.FilterSet):
    class Meta:
        model = Country
        fields = {
            'long_name': ['icontains'],
            'abbreviation': ['icontains']
        }

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filterset_class = CountryFilter
    filter_backends = [rest_framework_filters.SearchFilter,
                       filters.DjangoFilterBackend, 
                       rest_framework_filters.OrderingFilter]
    ordering_fields = ['created_on']
    ordering = ['-created_on']