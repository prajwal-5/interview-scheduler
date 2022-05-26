from django.contrib import admin
from .models import Interview, Participant
# Register your models here.

@admin.register(Interview)
class InterviewModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'start_time', 'end_time', 'participated_by']


@admin.register(Participant)
class ParticipantModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'position', 'email']