from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ExerciseSchedule,NutrationPlane,video
# Create your views here.
@login_required()
def premium(request):
    if request.user.is_authenticated:
        
       exercise=ExerciseSchedule.objects.filter(relation=request.user)
       nutration=NutrationPlane.objects.filter(relation=request.user)
       Video=video.objects.filter(relation=request.user)

    else:
       return redirect('login')
    return render(request, 'premium/premium.html',{'exercise':exercise,'nutration':nutration,'video': Video})