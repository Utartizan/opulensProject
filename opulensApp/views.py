from django.shortcuts import render, redirect
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

            # Save to the database
            user = UserAccount(username=username, email=email, password=password)
            user.save()

            return redirect('opulens')  # Redirect after successful registration
    else:
        form = RegisterForm()

    return render(request, 'signin.html', {'form': form})


def opulens(request):
    return render(request, 'opulens.html')  