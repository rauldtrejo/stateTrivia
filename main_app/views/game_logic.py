from main_app.models import State, Score, Progress, TotalScore
from django.shortcuts import render, redirect
from main_app.forms import StateForm
from random import shuffle
from django.contrib.auth.decorators import login_required


# The game view is the one responsible for the core gameplay of all 3 game modes
# It retrieves all the variables and objects needed for the game_logic html to function
# And works for all 3 game modes by accepting a game_mode parameter.
# To get shuffled answers for capitals and mottos game mode, first the code gets all states
# runs a for loop and appends all state objects to shuffle array, and shuffles them.
# Then it appends the current state correct answer into answer array, and runs a for loop
# that appends only 2 of the shuffled state objects into the answer array, and shuffles the answer array.
# the answer array gets passed on to the context object, and the proper game type html is loaded.
@login_required
def game(request, game_mode):
    user_progress = Progress.objects.get(user = request.user, game_mode = game_mode)
    state_id = user_progress.correct + user_progress.incorrect + 1
    if(state_id <= 50):
        all_states = State.objects.all()
        current_state = State.objects.get(id=state_id)
        next_state = current_state.id + 1
        state_form = StateForm()
        shuffleArray = []
        AnswerArray = []
        progress = (current_state.id/50)*100

        for state in all_states:
            shuffleArray.append(state)
        shuffle(shuffleArray)

        if(game_mode == 'capitals'):
            AnswerArray.append(current_state.capital)
            for x in range(2):
                AnswerArray.append(shuffleArray[x].capital)
        elif(game_mode == 'mottos'):
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
        'game_mode': game_mode,
        'state_form': state_form
        }

        if(game_mode == 'capitals'):
            return render (request, 'game_modes/capitals/capitals.html', context)
        elif(game_mode == 'mottos'):
            return render (request, 'game_modes/mottos/mottos.html', context)
        elif(game_mode == 'extreme'):
            return render (request, 'game_modes/extreme/extreme.html', context)
    else:
        return redirect('game_completed', game_mode = game_mode)

# This view is executed when a user decides to start a new game, either at the resume game modal
# or at the game completed screen.
@login_required
def new_game(request, game_mode):
    user_progress = Progress.objects.get(user = request.user, game_mode = game_mode)
    user_progress.correct = 0
    user_progress.incorrect = 0
    user_progress.save()
    return redirect('game', game_mode = game_mode)

# This view renders the game completed page that shows when a user answers all 50 states.
@login_required
def game_completed(request, game_mode):
    user_progress = Progress.objects.get(user = request.user, game_mode = game_mode)
    context = {
        'user_progress':user_progress,
        'game_mode': game_mode,
    }
    return render(request , 'game_modes/partials/game_completed.html', context)

# This view is executed when the user selects the correct answer in the Know the capital
# or know the motto game modes. It increments the correct answer counters in the user score
# models and redirects to the correct answer page view.
@login_required
def correct_answer(request, game_mode):
    user_progress = Progress.objects.get(
        user = request.user,
        game_mode = game_mode,
    )
    user_total_score, created = TotalScore.objects.get_or_create(
        user = request.user,
        game_mode = game_mode,
        defaults= {
            'total_score': 0,
        }
    )
    state_id = user_progress.correct + user_progress.incorrect + 1
    current_state = State.objects.get(id=state_id)
    user_score, created = Score.objects.get_or_create(
        user = request.user,
        game_mode = game_mode,
        state = current_state,
        defaults={
            'correct': 0,
            'incorrect': 0,
            'total_points': 0,
        }     
    )
    user_progress.correct += 1
    user_score.correct += 1
    user_score.total_points += 100
    user_total_score.total_score += 100
    user_progress.save()
    user_score.save()
    user_total_score.save()
    return redirect('correct_answer_page', game_mode = game_mode)

# This view renders the correct answer page of any given game mode by using a game mode parameter.
@login_required
def correct_answer_page(request, game_mode):
    user_progress = Progress.objects.get(user = request.user, game_mode = game_mode)
    state_id = user_progress.correct + user_progress.incorrect
    current_state = State.objects.get(id=state_id)
    next_state = current_state.id + 1
    progress = (current_state.id/50)*100
    context = {
        'current_state': current_state,
        'next_state': next_state,
        'progress': progress,
        'user_progress': user_progress,
        'game_mode': game_mode,
    }
    if(game_mode == 'capitals'):
        return render (request, 'game_modes/capitals/capitals_correct.html', context)
    elif(game_mode == 'mottos'):
        return render (request, 'game_modes/mottos/mottos_correct.html', context)
    elif(game_mode == 'extreme'):
        return render (request, 'game_modes/extreme/extreme_correct.html', context)

# This view is the inverse of correct answer, it runs when a user selects the incorrect answer
# It will increment the incorrect answer counters in the user total score and progress models.
# It then redirects to the incorrect answer page view.
@login_required
def incorrect_answer(request, game_mode):
    user_progress = Progress.objects.get(
        user = request.user,
        game_mode = game_mode,
    )
    user_total_score, created = TotalScore.objects.get_or_create(
        user = request.user,
        game_mode = game_mode,
        defaults= {
            'total_score': 0,
        }
    )
    state_id = user_progress.correct + user_progress.incorrect + 1
    current_state = State.objects.get(id=state_id)
    user_score, created = Score.objects.get_or_create(
        user = request.user,
        game_mode = game_mode,
        state = current_state,
        defaults={
            'correct': 0,
            'incorrect': 0,
            'total_points': 0,
        }     
    )
    user_progress.incorrect += 1
    user_score.incorrect += 1
    user_score.total_points -= 100
    user_total_score.total_score -= 100
    user_progress.save()
    user_score.save()
    user_total_score.save()
    return redirect('incorrect_answer_page', game_mode = game_mode)

# This view renders the incorrect answer page of any game mode by using a game mode parameter.
@login_required
def incorrect_answer_page(request, game_mode):
    user_progress = Progress.objects.get(user = request.user, game_mode = game_mode)
    state_id = user_progress.correct + user_progress.incorrect
    current_state = State.objects.get(id=state_id)
    next_state = current_state.id + 1
    progress = (current_state.id/50)*100
    context = {
        'current_state': current_state,
        'next_state': next_state,
        'progress': progress,
        'user_progress': user_progress,
        'game_mode': game_mode,
    }
    if(game_mode == 'capitals'):
        return render (request, 'game_modes/capitals/capitals_incorrect.html', context)
    elif(game_mode == 'mottos'):
        return render (request, 'game_modes/mottos/mottos_incorrect.html', context)
    elif(game_mode == 'extreme'):
        return render (request, 'game_modes/extreme/extreme_incorrect.html', context)
