from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Flare
from .forms import FlareForm

# Create your views here.

def index(request):
	flares = Flare.objects.all() 
	context = {'flares': flares}
	return render(request, 'website/index.html', context)

@login_required
def myListings(request):
	flares = Flare.objects.filter(owner=request.user).order_by('-date_added')
	context = {'flares': flares}
	return render(request, 'website/myListings.html', context)

def listings(request):
	if request.method == 'POST':

		id = request.POST.get("id", "")
		Flare.objects.get(pk=id).delete()

	flares = Flare.objects.order_by('-date_added')
	context = {'flares': flares}
	return render(request, 'website/listings.html', context)


def create(request):
	if request.method != 'POST':
		form = FlareForm()
	else:
		form = FlareForm(request.POST)
		if (form.is_valid()):
			new_flare = form.save(commit=False)
			if request.user.is_authenticated:
				new_flare.owner = request.user
			else:
				new_flare.owner = None
			new_flare.save()
		return HttpResponseRedirect(reverse('website:listings'))

	return render(request, 'website/create.html', {'form': form})


def filter(request, tag):
	
	flares = Flare.objects.filter(tags__contains=tag)

	if (len(flares) > 0):
		found = True
	else:
		found = False
		
	context = {'flares': flares, 'found': found}

	return render(request, 'website/filter.html', context)
 