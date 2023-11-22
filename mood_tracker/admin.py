from django.contrib import admin
from views.py import Achievements

# Register your models here.
@admin.register(Achievements):
class AchievementsAdmin(SummernoteModelAdmin):
    list_display = ('achievement_id', 'achievement_name', 'achievement_description')