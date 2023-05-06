from django.shortcuts import render


# Create your views here.
def guess_game(request):
    return render(request, 'guess_game.html')
