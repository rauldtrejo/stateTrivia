from main_app.models import State, Score, Progress
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from random import shuffle
from main_app.forms import StateForm


# Create your views here.

def home(request):
  if request.user.is_authenticated :
    user_progress_capitals, created = Progress.objects.get_or_create(
    user = request.user,
    game_mode = 'capitals',
    defaults={'correct': 0, 'incorrect':0}
    )
    user_left_off_capitals = user_progress_capitals.correct + user_progress_capitals.incorrect + 1

    user_progress_mottos, created = Progress.objects.get_or_create(
    user = request.user,
    game_mode = 'mottos',
    defaults={'correct': 0, 'incorrect':0}
    )
    user_left_off_mottos = user_progress_mottos.correct + user_progress_mottos.incorrect + 1

    user_progress_extreme, created = Progress.objects.get_or_create(
    user = request.user,
    game_mode = 'extreme',
    defaults={'correct': 0, 'incorrect':0}
    )
    user_left_off_extreme = user_progress_extreme.correct + user_progress_extreme.incorrect + 1

    context={
      'user_left_off_capitals' : user_left_off_capitals,
      'user_left_off_mottos' : user_left_off_mottos,
      'user_left_off_extreme' : user_left_off_extreme,
    }
    return render(request, 'landingPage.html', context)
  else:
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

    context = {
      'current_state': current_state,
      'next_state': next_state,
      'AnswerArray': AnswerArray,
      'progress': progress,
      'user_progress': user_progress
    }
    return render (request, 'gameModes/capitals/capitals.html', context)
  else:
    user_progress.correct = 0
    user_progress.incorrect = 0
    user_progress.save()
    return redirect('home')

def game_mottos(request, state_id):
  user_progress = Progress.objects.get(user = request.user, game_mode = 'mottos')
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

    AnswerArray.append(current_state.motto)
    for x in range(2):
      AnswerArray.append(shuffleArray[x].motto)

    shuffle(AnswerArray)

    context = {
      'current_state': current_state,
      'next_state': next_state,
      'AnswerArray': AnswerArray,
      'progress': progress,
      'user_progress': user_progress
    }
    return render (request, 'gameModes/mottos/mottos.html', context)
  else:
    user_progress.correct = 0
    user_progress.incorrect = 0
    user_progress.save()
    return redirect('home')

def game_extreme(request, state_id):
  user_progress = Progress.objects.get(user = request.user, game_mode = 'extreme')
  if(state_id <= 50):
    all_states = State.objects.all()
    current_state = State.objects.get(id=state_id)
    state_form = StateForm()
    next_state = current_state.id + 1
    shuffleArray = []
    AnswerArray = []
    progress = (current_state.id/50)*100

    for state in all_states:
      shuffleArray.append(state)

    shuffle(shuffleArray)

    AnswerArray.append(current_state.motto)
    for x in range(2):
      AnswerArray.append(shuffleArray[x].motto)

    shuffle(AnswerArray)

    context = {
      'current_state': current_state,
      'next_state': next_state,
      'AnswerArray': AnswerArray,
      'progress': progress,
      'user_progress': user_progress,
      'state_form': state_form
    }
    return render (request, 'gameModes/EXTREME/extreme.html', context)
  else:
    user_progress.correct = 0
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
  return render (request, 'gameModes/capitals/capitals_incorrect.html', context)


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
  return render (request, 'gameModes/capitals/capitals_correct.html', context)

def game_mottos_incorrect(request, state_id):
  user_progress = Progress.objects.get(user = request.user, game_mode = 'mottos')
  current_state = State.objects.get(id=state_id)
  next_state = current_state.id + 1
  progress = (current_state.id/50)*100
  context = {
    'current_state': current_state,
    'next_state': next_state,
    'progress': progress,
    'user_progress': user_progress
  }
  return render (request, 'gameModes/mottos/mottos_incorrect.html', context)


def game_mottos_correct(request, state_id):
  user_progress = Progress.objects.get(user = request.user, game_mode = 'mottos')
  current_state = State.objects.get(id=state_id)
  next_state = current_state.id + 1
  progress = (current_state.id/50)*100
  context = {
    'current_state': current_state,
    'next_state': next_state,
    'progress': progress,
    'user_progress': user_progress
  }
  return render (request, 'gameModes/mottos/mottos_correct.html', context)

def game_extreme_incorrect(request, state_id):
  user_progress = Progress.objects.get(user = request.user, game_mode = 'extreme')
  current_state = State.objects.get(id=state_id)
  next_state = current_state.id + 1
  progress = (current_state.id/50)*100
  context = {
    'current_state': current_state,
    'next_state': next_state,
    'progress': progress,
    'user_progress': user_progress
  }
  return render (request, 'gameModes/EXTREME/extreme_incorrect.html', context)


def game_extreme_correct(request, state_id):
  user_progress = Progress.objects.get(user = request.user, game_mode = 'extreme')
  current_state = State.objects.get(id=state_id)
  next_state = current_state.id + 1
  progress = (current_state.id/50)*100
  context = {
    'current_state': current_state,
    'next_state': next_state,
    'progress': progress,
    'user_progress': user_progress
  }
  return render (request, 'gameModes/EXTREME/extreme_correct.html', context)


def game_extreme_answer(request, state_id):
  current_state = State.objects.get(id=state_id)
  user_progress = Progress.objects.get(
  user = request.user,
  game_mode = 'extreme',
  )
  user_score, created = Score.objects.get_or_create(
  user = request.user,
  state = current_state,
  game_mode = 'extreme',
  defaults={'correct': 0, 'incorrect': 0, 'total_points': 0}  
  )
  state_form = StateForm(request.POST)
  answer= state_form.save(commit=False)
  if answer.name == current_state.name and answer.motto == current_state.motto and answer.capital == current_state.capital:
    user_score.correct += 1
    user_score.total_points +=100
    user_progress.correct += 1
    user_progress.save()
    return redirect('game_extreme_correct', state_id=state_id)
  else:
    user_score.incorrect += 1
    user_score.total_points -=100
    user_progress.incorrect += 1
    user_progress.save()
    return redirect('game_extreme_incorrect', state_id=state_id)



def game_capitals_correct_answer(request, state_id):
  user_progress, created = Progress.objects.get_or_create(
  user = request.user,
  game_mode = 'capitals',
  defaults={'correct': 0, 'incorrect':0}
  )
  user_progress.correct += 1
  user_progress.save()

  return redirect('game_capitals_correct', state_id=state_id)

def game_capitals_incorrect_answer(request, state_id):
  user_progress, created = Progress.objects.get_or_create(
  user = request.user,
  game_mode = 'capitals',
  defaults={'correct': 0, 'incorrect':0}
  )
  user_progress.incorrect += 1
  user_progress.save()

  return redirect('game_capitals_incorrect', state_id=state_id)

def game_mottos_correct_answer(request, state_id):
  user_progress, created = Progress.objects.get_or_create(
  user = request.user,
  game_mode = 'mottos',
  defaults={'correct': 0, 'incorrect':0}
  )
  current_state = State.objects.get(id=state_id)
  user_score, created = Score.objects.get_or_create(
  user = request.user,
  state = current_state,
  game_mode = 'mottos',
  defaults={'correct': 0, 'incorrect': 0, 'total_points': 0}  
  )
  user_progress.correct += 1
  user_score.correct += 1
  user_score.total_points +=100
  user_progress.save()
  user_score.save()

  return redirect('game_mottos_correct', state_id=state_id)

def game_mottos_incorrect_answer(request, state_id):
  user_progress, created = Progress.objects.get_or_create(
  user = request.user,
  game_mode = 'mottos',
  defaults={'correct': 0, 'incorrect':0}
  )
  user_progress.incorrect += 1
  user_progress.save()

  return redirect('game_mottos_incorrect', state_id=state_id)

