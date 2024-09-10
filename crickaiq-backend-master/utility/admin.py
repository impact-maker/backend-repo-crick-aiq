from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Prediction)
class PredictionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'user', 'country_b', 'format', 'match_date', 'banner_picture', 'result', 'status', 'created_on', 'modified_on')


@admin.register(Analysis)
class AnalysisAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'user', 'result', 'type', 'created_on', 'modified_on')
