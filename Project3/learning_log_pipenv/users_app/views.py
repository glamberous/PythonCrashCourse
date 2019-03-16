from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import logout

def logout_view(request):
    """ Log the user out """
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs_app:index'))
