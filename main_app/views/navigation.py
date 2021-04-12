from main_app.models import Progress, Score, TotalScore
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def home(request):
  if request.user.is_authenticated :
    user_progress_capitals, created = Progress.objects.get_or_create(
    user = request.user,
    game_mode = 'capitals',
    defaults={'correct': 0, 'incorrect':0}
    )
    user_progress_mottos, created = Progress.objects.get_or_create(
    user = request.user,
    game_mode = 'mottos',
    defaults={'correct': 0, 'incorrect':0}
    )
    user_progress_extreme, created = Progress.objects.get_or_create(
    user = request.user,
    game_mode = 'extreme',
    defaults={'correct': 0, 'incorrect':0}
    )
    context={
      'capitals' : 'capitals',
      'mottos': 'mottos',
      'extreme':'extreme',
    }
    return render(request, 'landingPage.html', context)
  else:
    return render(request, 'landingPage.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def user_score(request, game_mode):
    score = Score.objects.filter(user = request.user, game_mode = game_mode)
    total_score, created = TotalScore.objects.get_or_create(
        user = request.user,
        game_mode = game_mode,
        defaults={
            'total_score':0,
        }
    )
    context = {
        'score':score,
        'game_mode': game_mode,
        'total_score': total_score,
    }
    return render(request, 'scores/user_score.html', context)


def highscores(request):
    capitals_scores = TotalScore.objects.filter(game_mode = 'capitals')
    mottos_scores = TotalScore.objects.filter(game_mode = 'mottos')
    extreme_scores = TotalScore.objects.filter(game_mode = 'extreme')
    top_scores_capitals = []
    top_scores_mottos = []
    top_scores_extreme = []

    if(len(capitals_scores)>10):
        for x in range(10):
            top_scores_capitals.append(capitals_scores[x])
    else:
        for score in capitals_scores:
            top_scores_capitals.append(score)

    if(len(mottos_scores)>10):
        for x in range(10):
            top_scores_mottos.append(mottos_scores[x])
    else:
        for score in mottos_scores:
            top_scores_mottos.append(score)
            
    if(len(extreme_scores)>10):
        for x in range(10):
            top_scores_extreme.append(extreme_scores[x])
    else:
        for score in extreme_scores:
            top_scores_extreme.append(score)

    context = {
        'top_scores_capitals': top_scores_capitals,
        'top_scores_mottos': top_scores_mottos,
        'top_scores_extreme': top_scores_extreme,
    }
    return render(request, 'scores/highscores.html', context)

