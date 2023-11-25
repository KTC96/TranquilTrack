from .models import Diary
from django import forms
from django_summernote.widgets import SummernoteWidget

class DiaryForm(forms.ModelForm):


    class Meta:
        model = Diary
        fields = ( 'mood', 'sleep', 'title','date_created', 'content')
        widgets = {
            'content': SummernoteWidget
        }

