from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm
from .models import UserAccount

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Process the form data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            hashed_password = make_password(password)

            # Save to the database
            user = UserAccount(username=username, email=email, password=hashed_password)
            user.save()

            return redirect('opulens')  # Redirect after successful registration
    else:
        form = RegisterForm()

    return render(request, 'signin.html', {'form': form})


def opulens(request):
    return render(request, 'opulens.html')  

def reportsinsights(request):
    return render(request, 'reportsinsights.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def login(request):
    return render(request, 'login.html')

def userinput(request):
    return render(request, 'userinput.html')

def datavisualisation(request): 
    return render(request, 'datavisualisation.html')

def signin(request):   
    return render(request, 'signin.html')

def budgetracking(request):
    return render(request, 'budgetracking.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')

def contact(request):
    return render(request, 'contact.html')