from django.contrib import admin
from .models import Achievements
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Achievements)
class AchievementsAdmin(SummernoteModelAdmin):
    list_display = ('achievement_id', 'achievement_name', 'achievement_description')