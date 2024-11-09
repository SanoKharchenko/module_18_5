from django.shortcuts import render


# Create your views here.


def platform(request):
    return render(request, 'fourth_task/platform.html')


def games(request):
    game = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    contex = {
        'games': game
    }
    return render(request, 'fourth_task/games.html', contex)


def cart(request):
    return render(request, 'fourth_task/cart.html')
from django.shortcuts import render

# Create your views here.
