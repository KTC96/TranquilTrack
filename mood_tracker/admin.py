from django.contrib import admin
from .models import SupportLocations, Diary, Achievements
from django_summernote.admin import SummernoteModelAdmin
    
@admin.register(Diary)    
class DiaryAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(SupportLocations)




