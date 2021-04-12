from main_app.models import State, Score, Progress, TotalScore
from django.shortcuts import render, redirect
from main_app.forms import StateForm
from random import shuffle
from django.contrib.auth.decorators import login_required

# Create your views here.
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

@login_required
def new_game(request, game_mode):
    user_progress = Progress.objects.get(user = request.user, game_mode = game_mode)
    user_progress.correct = 0
    user_progress.incorrect = 0
    user_progress.save()
    return redirect('game', game_mode = game_mode)

@login_required
def game_completed(request, game_mode):
    user_progress = Progress.objects.get(user = request.user, game_mode = game_mode)
    context = {
        'user_progress':user_progress,
        'game_mode': game_mode,
    }
    return render(request , 'game_modes/partials/game_completed.html', context)

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
