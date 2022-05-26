from unicodedata import name
from django.db import models

# Create your models here.
POSITION_CHOICES = [
    ('Candidate', 'Candidate'), 
    ('Interviewer', 'Interviewer'),
]

class Participant(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=11, choices=POSITION_CHOICES, default='candidate')
    email = models.EmailField()

    def __str__(self):
        return self.name + " - " + self.position

    def pos(self):
        return self.position

class Interview(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    participants = models.ManyToManyField(Participant)

    def participated_by(self):
        return self.participants.all()