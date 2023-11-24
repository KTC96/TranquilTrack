from django.shortcuts import render, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Diary, Achievements, SupportLocations
from .forms import DiaryForm

class Home(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class Support(LoginRequiredMixin,TemplateView):
    template_name = 'support.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        locations = SupportLocations.objects.all()
        context['locations'] = locations 
        return context

class MoodtrackerView(LoginRequiredMixin,ListView):
    model = Diary
    template_name = "moodtracker.html"

class DiaryListView(LoginRequiredMixin,ListView):
    model = Diary
    queryset = Diary.objects.all().order_by("-date_created")
    template_name = "diary_list.html"
    paginate_by = 5

class DiaryDetailView(DetailView):
    model = Diary
    template_name = "diary_detail.html"

class AchievementListView(ListView):
    model = Achievements

class DiaryView(LoginRequiredMixin,CreateView):
    model = Diary
    template_name = "diary.html"
    form_class = DiaryForm

    def add_achievement(request):
        user = request.user

        diary_count = Diary.objects.count()
        achievements = Achievement.objects.filter(criteria__lte=diary_count)
        user.userprofile.achievements.set(achievements)

    def get_success_url(self):
        return reverse('diary_list')
        

class DiaryUpdateView(LoginRequiredMixin,UpdateView):
    
    model = Diary
    template_name = "diary_update.html"
    form_class = DiaryForm

    def get_success_url(self):
        return reverse('diary_list')


class DiaryDeleteView(LoginRequiredMixin,DeleteView):
    
    model = Diary
    template_name = "diary_delete.html"

    def get_success_url(self):
        return reverse('diary_list')

class DiaryUpdateView(LoginRequiredMixin,UpdateView):
    
    model = Diary
    template_name = "diary_update.html"
    form_class = DiaryForm

    def get_success_url(self):
        return reverse('diary_list')


def handle403(request, exception):
    return render(request, '403.html', status=403)


def handle404(request, exception):
    return render(request, '404.html', status=404)


def handle500(request):
    return render(request, '500.html', status=500)
