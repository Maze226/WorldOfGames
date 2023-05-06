from django.shortcuts import render


# Create your views here.
def memory_game(request):
    return render(request, 'memory_game.html')
