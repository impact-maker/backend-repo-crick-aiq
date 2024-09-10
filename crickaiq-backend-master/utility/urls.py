from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


prediction_router = DefaultRouter()
prediction_router.register(r"", views.PredictionViewSet, basename="prediction")

analysis_router = DefaultRouter()
analysis_router.register(r"", views.AnalysisViewSet, basename="analysis")


urlpatterns = [
    path("prediction/", include(prediction_router.urls)),
    path("analysis/", include(analysis_router.urls))
]