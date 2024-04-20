from django.shortcuts import render

def landing(request):
    return render(request, 'index.html')

def shop(request):
    return render(request, 'shop.html')

def contact(request):
    return render(request, 'contact.html')