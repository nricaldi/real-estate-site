from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        "all_listings": paged_listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    # current_listing = Listing.objects.get(id=listing_id)
    current_listing = get_object_or_404(Listing, pk=listing_id )

    context = {
        "listing": current_listing,
        "num": [1,2,3,4,5,6]
    }
    return render(request, 'listings/listing.html', context)

def search(request):

    return render(request, 'listings/search.html') 