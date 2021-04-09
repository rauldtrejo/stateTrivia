from django.http import request
from main_app.models import State
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Progress, State
from random import shuffle

# Create your views here.

def home(request):
  user_progress, created = Progress.objects.get_or_create(
  user = request.user,
  game_mode = 'capitals',
  defaults={'current_state': 0, 'incorrect':0}
  )
  user_left_off = user_progress.current_state + user_progress.incorrect + 1
  return render(request, 'landingPage.html', {'user_left_off': user_left_off})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  # A GET or a bad POST request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def game_capitals(request, state_id):
  user_progress = Progress.objects.get(user = request.user, game_mode = 'capitals')
  if(state_id <= 50):
    all_states = State.objects.all()
    current_state = State.objects.get(id=state_id)
    next_state = current_state.id + 1
    shuffleArray = []
    AnswerArray = []
    progress = (current_state.id/50)*100

    for state in all_states:
      shuffleArray.append(state)


    shuffle(shuffleArray)

    AnswerArray.append(current_state.capital)
    for x in range(2):
      AnswerArray.append(shuffleArray[x].capital)

    shuffle(AnswerArray)
    print(AnswerArray)

    context = {
      'current_state': current_state,
      'next_state': next_state,
      'AnswerArray': AnswerArray,
      'progress': progress,
      'user_progress': user_progress
    }
    return render (request, 'gameModes/capitals.html', context)
  else:
    user_progress.current_state = 0
    user_progress.incorrect = 0
    user_progress.save()
    return redirect('home')



def game_capitals_incorrect(request, state_id):
  user_progress = Progress.objects.get(user = request.user, game_mode = 'capitals')
  current_state = State.objects.get(id=state_id)
  next_state = current_state.id + 1
  progress = (current_state.id/50)*100
  context = {
    'current_state': current_state,
    'next_state': next_state,
    'progress': progress,
    'user_progress': user_progress
  }
  return render (request, 'gameModes/capitals_incorrect.html', context)


def game_capitals_correct(request, state_id):
  user_progress = Progress.objects.get(user = request.user, game_mode = 'capitals')
  current_state = State.objects.get(id=state_id)
  next_state = current_state.id + 1
  progress = (current_state.id/50)*100
  context = {
    'current_state': current_state,
    'next_state': next_state,
    'progress': progress,
    'user_progress': user_progress
  }
  return render (request, 'gameModes/capitals_correct.html', context)


def game_capitals_correct_answer(request, state_id):
  user_progress, created = Progress.objects.get_or_create(
  user = request.user,
  game_mode = 'capitals',
  defaults={'current_state': 0, 'incorrect':0}
  )
  user_progress.current_state += 1
  user_progress.save()

  return redirect('game_capitals_correct', state_id=state_id)

def game_capitals_incorrect_answer(request, state_id):
  user_progress, created = Progress.objects.get_or_create(
  user = request.user,
  game_mode = 'capitals',
  defaults={'current_state': 0, 'incorrect':0}
  )
  user_progress.incorrect += 1
  user_progress.save()

  return redirect('game_capitals_incorrect', state_id=state_id)

