from jobprofiles.models import UserProfile, CandidateProfile


def user_type(request):
    context = {
        'is_candidate': False,
        'candidate_id': None,
    }
    
    if not request.user.is_authenticated:
        return context
    
    try:
        user_profile = UserProfile.objects.get(user = request.user)
        context['is_candidate'] = user_profile.is_candidate()
        
        if context['is_candidate']:
            candidate_profile = CandidateProfile.objects.get(user_profile = user_profile)
            context['candidate_id'] = candidate_profile.id
        
        return context
    
    except(UserProfile.DoesNotExist, CandidateProfile.DoesNotExist):
        return context
            
        
        
    