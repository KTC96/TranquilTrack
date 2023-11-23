from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



class Home(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class Support(LoginRequiredMixin,TemplateView):
    template_name = 'support.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        locations = SupportLocations.objects.all()
        context['locations'] = locations 
        return context

class DiaryListView(LoginRequiredMixin,ListView):
    model = Diary
    queryset = Diary.objects.all().order_by("-date_created")
    template_name = "diary_list.html"
class DiaryDetailView(DetailView):
    model = Diary
    template_name = "diary_detail.html"


def handle403(request, exception):
    return render(request, '403.html', status=403)


def handle404(request, exception):
    return render(request, '404.html', status=404)


def handle500(request):
    return render(request, '500.html', status=500)
