from operator import pos
from tkinter import Widget
from turtle import position
from django.core import validators
from django import forms
from .models import Interview, Participant

class InterviewScheduling(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['date', 'start_time', 'end_time', 'participants']
        widgets = {
            'date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'start_time': forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
            'end_time': forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
            'participants': forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),
        }
    participants = forms.ModelMultipleChoiceField(
        queryset=Participant.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )