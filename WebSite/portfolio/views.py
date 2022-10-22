from django.shortcuts import render
from .models import Home,About,Category,Portfolio,profile

def index(request):

    home = Home.objects.latest('updated')

    about = About.objects.latest('updated')
    profiles = profile.objects.filter(about=about)

    categories = Category.objects.all()

    portfolios = Portfolio.objects.all()
    

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios
    }


    return render(request, 'index.html', context)
