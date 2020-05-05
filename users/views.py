# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    """Log the user out."""
    """django logout function:"""
    logout(request)
    return HttpResponseRedirect(reverse('website:index'))

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        #Display a blank registration form.
        form = UserCreationForm()
    else:
        #Process completed form.
        form = UserCreationForm(data=request.POST)

    if form.is_valid():
        new_user = form.save()
        # Log the user in and then redirect to home page.
        authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
        login(request, authenticated_user)
        return HttpResponseRedirect(reverse('website:index'))
    
    context = {'form': form}
    return render(request, 'users/register.html', context)

