from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



class Home(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class AchievementList(generic.ListView):
    model = Achievement
    queryset = Category.objects.order_by('-category_id')
    template_name = 'achievements.html'


