from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request): 
    recent_listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3] # :3 limits results to 3

    context = {
        "recent_listings": recent_listings
    }

    return render(request, 'pages/index.html', context)

def about(request): 
    all_realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        "all_realtors": all_realtors,
        "mvp_realtors": mvp_realtors
    }

    return render(request, 'pages/about.html', context)