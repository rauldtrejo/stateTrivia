from main_app.models import State, Score, Progress
from django.shortcuts import render, redirect
from main_app.forms import StateForm


# Create your views here.

def game_extreme_incorrect(request, game_mode):
  user_progress = Progress.objects.get(user = request.user, game_mode = game_mode)
  current_state = State.objects.get(id=state_id)
  next_state = current_state.id + 1
  progress = (current_state.id/50)*100
  context = {
    'current_state': current_state,
    'next_state': next_state,
    'progress': progress,
    'user_progress': user_progress
  }
  return render (request, 'game_modes/extreme/extreme_incorrect.html', context)


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
  return render (request, 'game_modes/extreme/extreme_correct.html', context)


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
  answer = state_form.save(commit=False)
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



