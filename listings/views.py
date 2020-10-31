from django.shortcuts import render
from .models import Listing

# Create your views here.
def index(request):
    listings = Listing.objects.all()

    context = {
        "all_listings": listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    current_listing = Listing.objects.get(id=listing_id)

    context = {
        "listing": current_listing
    }
    return render(request, 'listings/listing.html')

def search(request):

    return render(request, 'listings/search.html')