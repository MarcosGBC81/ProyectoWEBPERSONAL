from django.shortcuts import render
from .models import Portfolio, Profile


def portfolio(request):

    profile = Profile.objects.first()
    projects = Portfolio.objects.all()

    return render(request, 'portfolio/portfolio.html', {
        'projects': projects,
        'profile': profile
    })