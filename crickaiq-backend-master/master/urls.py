from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


country_router = DefaultRouter()
country_router.register(r"", views.CountryViewSet, basename="country")


urlpatterns = [
    path("country/", include(country_router.urls)),
]