from django.urls import path 
from .views import game_logic, profile

urlpatterns = [
    path('', game_logic.home, name='home'),
    path('accounts/signup', game_logic.signup, name='signup'),
    path('game/capitals/<int:state_id>/', game_logic.game_capitals, name='game_capitals'),
    path('game/capitals_correct/<int:state_id>', game_logic.game_capitals_correct, name='game_capitals_correct'),
    path('game/capitals_incorrect/<int:state_id>', game_logic.game_capitals_incorrect, name='game_capitals_incorrect'),
    path('game/capitals_correct_answer/<int:state_id>', game_logic.game_capitals_correct_answer, name='game_capitals_correct_answer'),
    path('game/capitals_incorrect_answer/<int:state_id>', game_logic.game_capitals_incorrect_answer, name='game_capitals_incorrect_answer'),
    path('game/mottos/<int:state_id>/', game_logic.game_mottos, name='game_mottos'),
    path('game/mottos_correct/<int:state_id>', game_logic.game_mottos_correct, name='game_mottos_correct'),
    path('game/mottos_incorrect/<int:state_id>', game_logic.game_mottos_incorrect, name='game_mottos_incorrect'),
    path('game/mottos_correct_answer/<int:state_id>', game_logic.game_mottos_correct_answer, name='game_mottos_correct_answer'),
    path('game/mottos_incorrect_answer/<int:state_id>', game_logic.game_mottos_incorrect_answer, name='game_mottos_incorrect_answer'),
    path('game/extreme/<int:state_id>/', game_logic.game_extreme, name='game_extreme'),
    path('game/extreme/answer/<int:state_id>/', game_logic.game_extreme_answer, name='game_extreme_answer'),
    path('game/extreme_correct/<int:state_id>/', game_logic.game_extreme_correct, name='game_extreme_correct'),
    path('game/extreme_incorrect/<int:state_id>/', game_logic.game_extreme_incorrect, name='game_extreme_incorrect'),

    path('user/profile', profile.profile_page, name='profile_page'),
    path('user/edit_username', profile.edit_username, name='edit_username'),
    path('user/edit_password', profile.edit_password, name='edit_password'),
    path('user/delete_account', profile.delete_account, name='delete_account'),
]
