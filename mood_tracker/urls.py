from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('support/', views.Support.as_view(),name='support'),
    path('mood_tracker/', views.MoodtrackerView.as_view(),name='mood_tracker'),
    path('diary/',views.DiaryView.as_view(),name='diary'),
    path('diary_list/',views.DiaryListView.as_view(),name='diary_list'),
    path("diary/<int:pk>",views.DiaryDetailView.as_view(),name ='diary_detail'),
    path("diary_update/<int:pk>",views.DiaryUpdateView.as_view(),name ='diary_update'),
    path("diary_delete/<int:pk>",views.DiaryDeleteView.as_view(),name ='diary_delete'),
]