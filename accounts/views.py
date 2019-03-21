from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

# Registration Logic and validation
def register(request):
  if request.method == 'POST':

    # Get values form
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Checking passwords match
    if password == password2:
      # Check Username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'The username has already taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'The email is being used')
          return redirect('register')
        else:
          # If it's correct
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.save()
          messages.success(request, 'You are now registered! Please do the login')
          return redirect('login')
    else:
      messages.error(request, 'Password do not match')
      return redirect('register')
  else:
    return render(request, 'accounts/register.html')

# Login Logic and validation
def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

# If statement for user to login
    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')

# Logout form request 
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'Your are now logged out')
        return redirect('index')

# Dashboard form lists
def dashboard(request):
  user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

  context = {
    'contacts': user_contacts
  }
  return render(request, 'accounts/dashboard.html', context)

