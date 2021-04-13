from main_app.models import Progress, Score, TotalScore
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# This view renders the homepage. It also creates user progress objects in the database
# for each game type, which avoids bugs if the user has no progress because he hasn't played yet.
# The user progress variables also serve to check if a user has a previous game started
# The home page has if statements that will check the value of this progress and ask the user if
# they wish to resume the previos game or start a new one.
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
      'user_progress_capitals': user_progress_capitals,
      'user_progress_mottos' : user_progress_mottos,
      'user_progress_extreme' : user_progress_extreme,
    }
    return render(request, 'landingPage.html', context)
  else:
    return render(request, 'landingPage.html')

# This view renders the sign up page, and handles the creation of a new user.
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

# This view renders the highscores page, the if statements check if there is more than 10 scores
# for any game mode and will only pick the top 10. If there is less than 10, it will grab all scores.

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

def about(request):
    return render(request,'about.html')

