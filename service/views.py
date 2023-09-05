from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Category, AllService, Letter
from .forms import Paper


def home(request):
    cat = Category.objects.all()
    serv = AllService.objects.all()
    if request.method == 'POST':
        form = Paper(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            person = Letter(email=email)
            person.save()
            return redirect('HOME')
        else:
            messages.error(request, 'با سپاس از مشارکت شما')
            return redirect('HOME')
    else:
        form = Paper()
    return render(request, "index.html", {'category':cat, 'services': serv, 'form':form})


def eachCategory(request, slug):
    cat = Category.objects.get(slug=slug)
    serv = AllService.objects.filter(category__slug=slug)
    return render(request, "each_category.html", {'category':cat, 'services':serv})


def allService(request):
    serv = AllService.objects.all()
    return render(request, "allservice.html", {'services': serv})


def eachService(request, slug):
    serv = AllService.objects.get(slug=slug)
    return render(request, "service.html", {'service':serv})
