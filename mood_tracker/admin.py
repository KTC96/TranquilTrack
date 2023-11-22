from django.contrib import admin
from .models import SupportLocations
from django_summernote.admin import SummernoteModelAdmin

@admin.register(SupportLocations)
class SupportAdmin(SummernoteModelAdmin):
    summernote_fields = ('details')
    
    
