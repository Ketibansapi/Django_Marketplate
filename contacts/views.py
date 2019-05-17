from django.shortcuts import render, redirect     
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Contact request for user to input the data
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

    #  Checker, if user has already made inquiries
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'Ops! You have already made inquiry for this property')
        return redirect('/')

    # Var matching contacts
    contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()

    # Send and receives mail using Google SMTP
    send_mail(
      'Property Listing Inquiry Notification',
      'Good day! There has been an inquiry for [' + listing + '] Go check with admin to see more information and please contact the seeker to get negotiation. Thank you. Regards, Lovely Admin', 
      'chickenflakes9@gmail.com',
      [realtor_email, 'deary2706@gmail.com'],
      fail_silently=False
    )

    # Success Messages
    messages.success(request, 'Your inquiry has been submitted, a realtor may contact you as soon as possible')
    return redirect('/')