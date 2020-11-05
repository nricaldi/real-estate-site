from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

import smtplib

# Create your views here.
def contact(request):

    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']



        # check if user has already made an inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('../listings/'+str(listing_id))
        


        # Create contact object and save
        # contact = Contact.objects.create(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )
        contact.save()

        # Send mail DOES NOT WORK, 
        ########################    ConnectionRefusedError: [Errno 61] Connection refused django senmail    #########################
        send_mail(
            'Propery Listing Inquiry',
            'There has been an inquiry for ' + listing + 'Sign in to the admin area for more info',
            'narman0799@gmail.com',
            [realtor_email, 'nricaldi.nr@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, 'Your request has been submitted. A realtor will get back to you as soon as possible.')

    return redirect('../listings/'+str(listing_id))