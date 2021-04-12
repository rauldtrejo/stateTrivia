from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from main_app.forms import UsernameForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from main_app.models import Score, TotalScore
from django.contrib.auth.decorators import login_required

@login_required
def profile_page(request):
    username_form = UsernameForm()
    password_form = PasswordChangeForm(user=request.user)
    context= {
        'username_form': username_form,
        'password_form': password_form,
    }
    return render(request, 'profile.html', context)

@login_required
def edit_username(request):
    username_form = UsernameForm(request.POST, instance=request.user)
    if request.POST:
        username_form.save()
        return redirect ('profile_page')

@login_required
def edit_password(request):
    password_form = PasswordChangeForm(user=request.user, data=request.POST)
    if request.POST and password_form.is_valid():
        password_form.save()
        update_session_auth_hash(request, password_form.user)
        return redirect ('profile_page')

@login_required
def delete_account(request):
    user = User.objects.get(username = request.user.username)
    user.delete()         
    return redirect('home')

@login_required
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
