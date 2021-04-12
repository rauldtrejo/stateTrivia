from django.urls import path 
from .views import game_logic, profile, navigation, extreme

urlpatterns = [
    path('', navigation.home, name='home'),
    path('accounts/signup', navigation.signup, name='signup'),
    path('user/score/<str:game_mode>/', navigation.user_score, name='user_score'),
    path('highscores/', navigation.highscores, name='highscores'),

    path('game/<str:game_mode>/', game_logic.game, name='game'),
    path('correct_answer/<str:game_mode>/', game_logic.correct_answer, name='correct_answer'),
    path('incorrect_answer/<str:game_mode>/', game_logic.incorrect_answer, name='incorrect_answer'),
    path('correct_answer_page/<str:game_mode>/', game_logic.correct_answer_page, name='correct_answer_page'),
    path('incorrect_answer_page/<str:game_mode>/', game_logic.incorrect_answer_page, name='incorrect_answer_page'),
    path('game/extreme/answer/<str:game_mode>/', extreme.answer, name='game_extreme_answer'),

    path('user/profile', profile.profile_page, name='profile_page'),
    path('user/edit_username', profile.edit_username, name='edit_username'),
    path('user/edit_password', profile.edit_password, name='edit_password'),
    path('user/delete_account', profile.delete_account, name='delete_account'),

]
