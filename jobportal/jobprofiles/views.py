from django.shortcuts import render
from .models import CandidateProfile
from utilities.paginator_page import paginate_queryset

def candidate_profile(request, candidate_id):
    candidate = CandidateProfile.objects.get(id = candidate_id)
    context = {
        'candidate': candidate,
    }
    return render(request, 'jobprofiles/candidate_profile.html', context)


def candidate_applied_jobs(request, candidate_id):
    candidate = CandidateProfile.objects.get(id = candidate_id)
    applied_jobList = candidate.applied_jobs.all()
    applied_jobs = paginate_queryset(request, applied_jobList, 3)
    
    context = {
        'candidate': candidate,
        'applied_jobs': applied_jobs,
    }
    
    return render(request, 'jobprofiles/candidate_applied_jobs.html', context)
    
    
def candidate_saved_jobs(request, candidate_id):
    candidate = CandidateProfile.objects.get(id = candidate_id)
    saved_jobList = candidate.favorited_jobs.all()
    savedJobs = paginate_queryset(request, saved_jobList, 2)
    
    context = {
        'candidate': candidate,
        'savedJobs': savedJobs,
    }
    
    return render(request, 'jobprofiles/candidate_saved_jobs.html', context)
    