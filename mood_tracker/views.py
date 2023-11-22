from django.shortcuts import render

class Home(TemplateView):
    template_name = 'index.html'
