from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date')
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        "all_listings": paged_listings
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