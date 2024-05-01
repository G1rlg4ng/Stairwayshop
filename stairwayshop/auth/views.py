from django.shortcuts import render, redirect
from . forms import RegistrationForm
from django.contrib import messages

# Registration view
def register(request):
    if request.method == "POST":
        form= RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successfull')
            return redirect('home-url')
    else:
        form=RegistrationForm()
    return render(request, 'auth/register.html', {"form":form})
