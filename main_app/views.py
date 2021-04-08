from django.http import request
from main_app.models import State
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import State
from random import shuffle

# Create your views here.

def home(request):
  return render(request, 'landingPage.html')

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
      'progress': progress
    }
    print(context)
    return render (request, 'gameModes/capitals.html', context)
  else:
    return redirect('home')



def game_capitals_incorrect(request, state_id):
  current_state = State.objects.get(id=state_id)
  next_state = current_state.id + 1
  context = {
    'current_state': current_state,
    'next_state': next_state,
  }
  return render (request, 'gameModes/capitals_incorrect.html', context)


