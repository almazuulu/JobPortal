from jobprofiles.models import UserProfile, CandidateProfile, CompanyProfile


def user_type(request):
    context = {
        'is_candidate': False,
        'candidate_id': None,
        'candidate': None,
        'is_company': False,
        'company_id': None,
        'company': None
    }
    
    if not request.user.is_authenticated:
        return context
    
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        context['is_candidate'] = user_profile.is_candidate()
        
        if context['is_candidate']:
            candidate_profile = CandidateProfile.objects.get(user_profile=user_profile)
            context['candidate_id'] = candidate_profile.id
            context['candidate'] = candidate_profile
        else:
            # Если этот объект не кандидат, проверяем явл-ся ли он компнией
            try:
                company_profile = CompanyProfile.objects.get(user_profile=user_profile)
                context['is_company'] = True # Если объект CompanyProfile найдет, устанавливаем True
                context['company_id'] = company_profile.id
                context['company'] = company_profile
                
            except CompanyProfile.DoesNotExist:
                pass
            
        return context 
    
    except UserProfile.DoesNotExist:
        return context
    
                
                

        
    
    
    
    
    # if not request.user.is_authenticated:
    #     return context
    
    # try:
    #     user_profile = UserProfile.objects.get(user = request.user)
    #     context['is_candidate'] = user_profile.is_candidate()
        
    #     if context['is_candidate']:
    #         candidate_profile = CandidateProfile.objects.get(user_profile = user_profile)
    #         context['candidate_id'] = candidate_profile.id
    #         context['candidate']  = candidate_profile
    #     return context
    
    # except(UserProfile.DoesNotExist, CandidateProfile.DoesNotExist):
    #     return context
            
        
        
    