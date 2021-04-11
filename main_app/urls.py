from django.urls import path 
from .views import game_logic, profile, navigation, game_logic_test

urlpatterns = [
    path('', navigation.home, name='home'),
    path('accounts/signup', navigation.signup, name='signup'),

    path('game/<str:game_mode>/', game_logic_test.game, name='game'),
    path('correct_answer/<str:game_mode>/', game_logic_test.correct_answer, name='correct_answer'),
    path('incorrect_answer/<str:game_mode>/', game_logic_test.incorrect_answer, name='incorrect_answer'),
    path('correct_answer_page/<str:game_mode>/', game_logic_test.correct_answer_page, name='correct_answer_page'),
    path('incorrect_answer_page/<str:game_mode>/', game_logic_test.incorrect_answer_page, name='incorrect_answer_page'),

    path('game/extreme/answer/<int:state_id>/', game_logic.game_extreme_answer, name='game_extreme_answer'),
    path('game/extreme_correct/<int:state_id>/', game_logic.game_extreme_correct, name='game_extreme_correct'),
    path('game/extreme_incorrect/<int:state_id>/', game_logic.game_extreme_incorrect, name='game_extreme_incorrect'),

    path('user/profile', profile.profile_page, name='profile_page'),
    path('user/edit_username', profile.edit_username, name='edit_username'),
    path('user/edit_password', profile.edit_password, name='edit_password'),
    path('user/delete_account', profile.delete_account, name='delete_account'),
]
