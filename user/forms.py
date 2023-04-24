from django import forms
from .models import Report,SolvedImage

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        exclude = ('user','issue_status','vote_count','issue','solved_image',)

class LtdAdmin(forms.ModelForm):
    class Meta:
         model=SolvedImage
         fields = ('solved_image',)
         
         