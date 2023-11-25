import json

from django.shortcuts import render, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Diary, SupportLocations, Achievements
from .forms import DiaryForm


class Home(LoginRequiredMixin, TemplateView):
    """
    This is to render the homepage once logged in
    It was changed from TemplateView to ListView to gather data from db
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """
        Gathers diary data from db to be sent to index.html template file
        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)

        context['data'] = json.dumps(
            [
                {
                    'id': obj.id,
                    'title': obj.title,
                    'content': obj.content,
                    'date_created': obj.date_created.isoformat().split('T')[0],
                    'mood': obj.mood,
                    'sleep': obj.sleep
                }
                for obj in Diary.objects.all()
            ]
        )

        return context


class Support(LoginRequiredMixin, TemplateView):
    template_name = 'support.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        locations = SupportLocations.objects.all()
        context['locations'] = locations
        return context


class MoodtrackerView(LoginRequiredMixin, ListView):
    model = Diary
    template_name = "moodtracker.html"


class DiaryListView(LoginRequiredMixin, ListView):
    template_name = "diary_list.html"
    paginate_by = 5

    def get_queryset(self):
        model = Diary
        user = self.request.user
        queryset = Diary.objects.filter(owner=user).order_by("-date_created")
        return queryset

class DiaryDetailView(DetailView):
    model = Diary
    template_name = "diary_detail.html"


class DiaryView(LoginRequiredMixin, CreateView):
    model = Diary
    template_name = "diary.html"
    form_class = DiaryForm

    def get_success_url(self):
        user = self.request.user
        diary_count = Diary.objects.filter(owner=user).count()
        first_achievement_exists = Achievements.objects.filter(achievement_name='First Diary Entry Made!').exists()
        second_achievement_exists = Achievements.objects.filter(achievement_name='5 Entries Made!').exists()
        third_achievement_exists = Achievements.objects.filter(achievement_name='10 Entries Made!').exists()
        if first_achievement_exists:
            if diary_count % 5 == 0:
                Achievements.objects.create(achievement_user=user, achievement_name='10 Entries Made!', achievement_description='Congrats! You made 10 diary entries') if second_achievement_exists else Achievements.objects.create(achievement_user=user, achievement_name='5 Entries Made!', achievement_description='Congrats! You made 5 diary entries')
        else:
            Achievements.objects.create(achievement_user=user, achievement_name='First Diary Entry Made!', achievement_description='Congrats! You made your first Diary entry')

        return reverse('diary_list')


class DiaryUpdateView(LoginRequiredMixin, UpdateView):
    model = Diary
    template_name = "diary_update.html"
    form_class = DiaryForm

    def get_success_url(self):
        return reverse('diary_list')


class DiaryDeleteView(LoginRequiredMixin, DeleteView):
    model = Diary
    template_name = "diary_delete.html"

    def get_success_url(self):
        return reverse('diary_list')

class AchievementListView(LoginRequiredMixin, ListView):
    template_name = "achievements_list.html"
    model = Achievements

    def get_queryset(self):
        user = self.request.user
        queryset = Achievements.objects.filter(achievement_user=user)
        print(queryset)
        return queryset

def handle403(request, exception):
    return render(request, '403.html', status=403)


def handle404(request, exception):
    return render(request, '404.html', status=404)


def handle500(request):
    return render(request, '500.html', status=500)
