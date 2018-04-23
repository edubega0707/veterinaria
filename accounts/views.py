from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Profile
#from .forms import UserRegistrationForm. ProfileForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class ProfileView(View):
    @method_decorator(login_required)
    def get(self, request):
        queryset=Profile.objects.get(id=request.user.profile.id)
        template_name='profile.html'
        context={
            'profile':queryset
        }

        return render(request,template_name, context)



