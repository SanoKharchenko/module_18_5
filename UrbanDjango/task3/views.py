from django.shortcuts import render


# Create your views here.


def platform(request):
    return render(request, 'third_task/platform.html')


def games(request):
    items = {
        'Atomic Heart': "Описание игры 1",
        'Cyberpunk 2077': "Описание игры 2",
        'PayDay 2': "Осисание игры 3",
    }
    return render(request, 'third_task/games.html', {'items': items})


def cart(request):
    return render(request, 'third_task/cart.html')
