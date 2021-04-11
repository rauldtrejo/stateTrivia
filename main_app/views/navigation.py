from main_app.models import Progress
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
    user_left_off_extreme = user_progress_extreme.correct + user_progress_extreme.incorrect + 1
    context={
      'user_left_off_extreme' : user_left_off_extreme,
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