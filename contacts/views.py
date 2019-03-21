from django.shortcuts import render, redirect     
from django.contrib import messages
#from django.core.mail import send_mail
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

    #  Checker, if user has already made inquiry or not
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'Ops! You have already made inquiry for this property')
        return redirect('/listings/'+listing_id)

    # Var matching
    contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()

    # Messages success
    messages.success(request, 'Your inquiry has been submitted, a realtor may contact you as soon as possible')
    return redirect('/listings/'+listing_id)
