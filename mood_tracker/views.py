from django.shortcuts import render, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
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


class DiaryView(LoginRequiredMixin,CreateView):
    model = Diary
    template_name = "diary.html"
    form_class = DiaryForm

    def get_success_url(self):
        return reverse('diary_list')
  
    # def diary(request):  
    #     if request.POST == 'POST':  
    #         form = DiaryForm()  
    #         if form.is_valid():  
    #             form.save()  
    
    #     else:  
    #         form = DiaryForm()  
    #     context = {  
    #         'form':form  
    #     }  
    #     return render(request, 'diary.html', context)  