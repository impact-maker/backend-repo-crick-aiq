from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'object_id', 'long_name', 'abbreviation', 'image_url', 'link_code', 'created_on', 'modified_on')
