from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('support/', views.Support.as_view(),name='support'),
    path('diary_list/',views.DiaryListView.as_view(),name='diary_list'),
    path("diary/<int:pk>",views.DiaryDetailView.as_view(),name ='diary_detail'),
]