from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from main.models import Scoreboard
from main.forms import ScoreForm


def index(request):
    return render(request, 'index.html')


def game(request):

    if request.method == 'POST':
        form = ScoreForm(request.POST)

        if form.is_valid():
            score = Scoreboard()
            score.username = form.cleaned_data['username']
            score.score = form.cleaned_data['score']
            score.save()

            return HttpResponseRedirect('/scoreboard/')
    else:
        form = ScoreForm()

    return render(request, 'game.html', {'form': form})


def scoreboard(request):
    all_scores = Scoreboard.objects.all()
    return render(request, 'scoreboard.html', context={"all_scores": all_scores})

