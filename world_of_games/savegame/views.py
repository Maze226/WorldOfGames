from django.shortcuts import render


# Create your views here.
def save_game(request):
    return render(request, 'save_game.html')
