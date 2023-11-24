from django.contrib import admin
from .models import Achievements
from django_summernote.admin import SummernoteModelAdmin
from .models import Diary, SupportLocations, Achievements
    
@admin.register(Diary)    
class DiaryAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

@admin.register(Achievements)    
class DiaryAdmin(SummernoteModelAdmin):
    summernote_fields = ('achievement_title',)

admin.site.register(SupportLocations)




