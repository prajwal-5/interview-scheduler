from datetime import timedelta
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import InterviewScheduling
from .models import Interview, Participant
from django.contrib import messages

# Home page view

def overlap(first_inter,second_inter):
    for f,s in ((first_inter,second_inter), (second_inter,first_inter)):
        for time in (f["starting_time"], f["ending_time"]):
            if s["starting_time"] <= time <= s["ending_time"]:
                return True
    else:
        return False

def home(req):
    if req.method == 'POST':
        fm = InterviewScheduling(req.POST)
        if fm.is_valid():
            pp = fm.cleaned_data['participants']
            stime = fm.cleaned_data['start_time']
            etime = fm.cleaned_data['end_time']
            mdate = fm.cleaned_data['date']

            if(pp.count()>1):
                candidate = False
                interviewer = False
                time = True
                for p in pp:
                    if p.position=="Candidate": 
                        candidate=True
                    if p.position=='Interviewer':
                        interviewer=True
                    if candidate and interviewer: 
                        break


                if(candidate and interviewer):
                    for p in pp:
                        schedule = Interview.objects.filter(participants__in=[p])
                        for slot in schedule:
                            farg = {
                                "starting_time":slot.start_time,
                                "ending_time":slot.end_time
                            }

                            sarg = {
                                "starting_time":stime,
                                "ending_time":etime
                            }

                            if (slot.date==mdate or slot.date+timedelta(days=1) == mdate) and overlap(farg, sarg):
                                time=False
                                msg = "{} has an interview from {} to {}"
                                participant_list = type(slot)
                                print(participant_list)
                                messages.warning(req, msg.format(p.name,slot.start_time,slot.end_time))                    

                if time and candidate and interviewer:
                    fm.save()
                    fm = InterviewScheduling()
                elif candidate==False or interviewer==False:
                    messages.warning(req, 'At least 1 Interviewer and 1 Candidate is required') 
            else:
                messages.warning(req, 'Number of participants is less than 2')
    else:
        fm = InterviewScheduling()
    interviews = Interview.objects.all()
    return render(req, "./home.html", {'form':fm, 'interviews':interviews})


# Edit Interview view
def edit_interview(req, id):
    if(req.method=='POST'):
        pi = Interview.objects.get(pk=id)
        fm = InterviewScheduling(req.POST, instance=pi)
        if fm.is_valid():
            pp = fm.cleaned_data['participants']
            stime = fm.cleaned_data['start_time']
            etime = fm.cleaned_data['end_time']
            mdate = fm.cleaned_data['date']
            if(pp.count()>1):
                candidate = False
                interviewer = False
                time = True
                for p in pp:
                   if p.position=="Candidate": 
                       candidate=True
                   if p.position=='Interviewer':
                       interviewer=True
                   if candidate and interviewer: 
                       break
               
                if(candidate and interviewer):
                   for p in pp:
                       schedule = Interview.objects.filter(participants__in=[p])
                       for slot in schedule:
                           farg = {
                               "starting_time":slot.start_time,
                               "ending_time":slot.end_time
                           }
                           sarg = {
                               "starting_time":stime,
                               "ending_time":etime
                           }
                           if (slot.date==mdate or slot.date+timedelta(days=1) == mdate) and overlap(farg, sarg):
                               time=False
                               msg = "{} has an interview from {} to {}"
                               participant_list = type(slot)
                               print(participant_list)
                               messages.warning(req, msg.format(p.name,slot.start_time,slot.end_time))                    
                if time and candidate and interviewer:
                   fm.save()
                   fm = InterviewScheduling()
                elif candidate==False or interviewer==False:
                   messages.warning(req, 'At least 1 Interviewer and 1 Candidate is required') 
            else:
                messages.warning(req, 'Number of participants is less than 2')
    else:
        pi = Interview.objects.get(pk=id)
        fm = InterviewScheduling(instance=pi)
    return render(req, "./edit_interview.html", {'form':fm})


# Delete Funcitionality 
def delete_interview(req, id):
    if(req.method == 'POST'):
        pi = Interview.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


# Verify Email
def verify(req, id):
    if req.method=="POST":
        pi = Interview.objects.get(pk=id).participated_by()
        etc = req.POST["emailtocheck"]
        check=False
        for p in pi:
            if(p.email.lower()==etc.lower()):
                messages.success(req, 'You are eligible for the Interview') 
                check=True
        
        
        if check==False: 
            messages.warning(req, "You are not eligible for interview")
    return render(req, "verify_ip.html")