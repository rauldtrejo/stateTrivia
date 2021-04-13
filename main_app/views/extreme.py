from main_app.models import State, Score, Progress, TotalScore
from django.shortcuts import redirect
from main_app.forms import StateForm
from django.contrib.auth.decorators import login_required


# Create your views here.

# The Answer view is executed when a user submits an answer during the extreme game mode
# It fetches the user progress for extreme mode from the database and uses it to establish
# the state_id of the current state.
# Then it fetches the user score for that individual state, and also the users total score 
# for the game mode. It then compares the answeres subimitted in the form to the current state
# object to verify that all 3 answers are correct or incorrect and will add or substract points to the user.
# After that it redirects to the correct_answer_page view, which renders the correct answer page.
@login_required
def answer(request, game_mode):
  user_progress = Progress.objects.get(
        user = request.user,
        game_mode = game_mode,
    )
  state_id = user_progress.correct + user_progress.incorrect + 1
  current_state = State.objects.get(id=state_id)
  user_score, created = Score.objects.get_or_create(
  user = request.user,
  state = current_state,
  game_mode = game_mode,
  defaults={'correct': 0, 'incorrect': 0, 'total_points': 0}  
  )
  user_total_score, created = TotalScore.objects.get_or_create(
    user = request.user,
    game_mode = game_mode,
    defaults= {
      'total_score': 0,
    }
  )
  state_form = StateForm(request.POST)
  answer = state_form.save(commit=False)
  if answer.name == current_state.name and answer.motto == current_state.motto and answer.capital == current_state.capital:
    user_score.correct += 1
    user_score.total_points +=100
    user_total_score.total_score += 100
    user_progress.correct += 1
    user_progress.save()
    user_score.save()
    user_total_score.save()
    return redirect('correct_answer_page', game_mode = game_mode)
  else:
    user_score.incorrect += 1
    user_score.total_points -=100
    user_progress.incorrect += 1
    user_total_score.total_score -= 100
    user_progress.save()
    user_score.save()
    user_total_score.save()
    return redirect('incorrect_answer_page', game_mode = game_mode)



