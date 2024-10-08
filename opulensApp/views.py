from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.hashers import make_password # type: ignore
from django.contrib.auth import authenticate, login # type: ignore
from .forms import RegisterForm
from .models import UserAccount
from .forms import EmailOrUsernameLoginForm # type: ignore
from django.contrib.auth.hashers import check_password # type: ignore
from django import forms # type: ignore
from .forms import BudgetEntryForm
from .models import BudgetEntry
from django.http import JsonResponse # type: ignore
from django.contrib.auth.decorators import login_required


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


def login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        print(f'Trying to log in with: {username_or_email} and password: {password}')

        # Attempt to retrieve the user based on username or email
        try:
            user = UserAccount.objects.get(username=username_or_email)  # Check by username
        except UserAccount.DoesNotExist:
            try:
                user = UserAccount.objects.get(email=username_or_email)  # Check by email
            except UserAccount.DoesNotExist:
                user = None  # No user found

        # Verify the password if the user exists
        if user is not None:
            if check_password(password, user.password):  # Compare the entered password with the stored hashed password
                print('Login successful!')
                request.session['user_id'] = user.id  # Save user ID in session
                return redirect('dashboard')  # Redirect to the dashboard
            else:
                print('Password is incorrect!')  # Password mismatch
        else:
            print('User does not exist!')  # User not found

        # If we reach here, there was an authentication error
        return render(request, 'login.html', {'error': 'Invalid username/email or password'})

    return render(request, 'login.html')  # Handle GET requests


def budgetTracking(request):
    print("Request method:", request.method)
    if request.method == 'POST':
        form = BudgetEntryForm(request.POST)
        print("Form data:", request.POST)
        if form.is_valid():
            print("Form is valid")
            category = form.cleaned_data['category']
            amount = form.cleaned_data['amount']
            description = form.cleaned_data.get('description', '')
            date = form.cleaned_data['date']

            # Save the budget entry
            budget_entry = BudgetEntry(category=category, amount=amount, description=description, date=date)
            budget_entry.save()

            # Return a JSON response indicating success
            return JsonResponse({'success': True})
        
        print("Form is not valid:", form.errors)
        return JsonResponse({'success': False, 'errors': form.errors})

    return JsonResponse({'success': False, 'errors': 'Invalid request.'})




def opulens(request):
    return render(request, 'opulens.html')  

@login_required
def reportsinsights(request):
    return render(request, 'reportsinsights.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def userinput(request):
    return render(request, 'userinput.html')

@login_required
def datavisualisation(request): 
    return render(request, 'datavisualisation.html')

def signin(request):   
    return render(request, 'signin.html')

@login_required
def budgetracking(request):
    return render(request, 'budgetracking.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')

def contact(request):
    return render(request, 'contact.html')