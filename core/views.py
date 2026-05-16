from django.shortcuts import render, HttpResponse
from portfolio.models import Profile
from .models import Persona

def home(request):

    profile = Profile.objects.first()
    persona = Persona.objects.first()

    return render(request, 'core/home.html', {
        'profile': profile,
        'persona': persona
    })


def about(request):

    profile = Profile.objects.first()
    persona = Persona.objects.first()

    return render(request, "core/about.html", {
        'profile': profile,
        'persona': persona
    })


def portfolio(request):

    profile = Profile.objects.first()
    persona = Persona.objects.first()

    return render(request, "core/../portfolio/templates/portfolio/portfolio.html", {
        'profile': profile,
        'persona': persona
    })


def contact(request):

    profile = Profile.objects.first()
    persona = Persona.objects.first()

    return render(request, "core/contact.html", {
        'profile': profile,
        'persona': persona
    })