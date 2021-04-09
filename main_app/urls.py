from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup', views.signup, name='signup'),
    path('game/capitals/<int:state_id>/', views.game_capitals, name='game_capitals'),
    path('game/capitals_correct/<int:state_id>', views.game_capitals_correct, name='game_capitals_correct'),
    path('game/capitals_incorrect/<int:state_id>', views.game_capitals_incorrect, name='game_capitals_incorrect'),
    path('game/capitals_correct_answer/<int:state_id>', views.game_capitals_correct_answer, name='game_capitals_correct_answer'),
    path('game/capitals_incorrect_answer/<int:state_id>', views.game_capitals_incorrect_answer, name='game_capitals_incorrect_answer'),
    path('game/mottos/<int:state_id>/', views.game_mottos, name='game_mottos'),
    path('game/mottos_correct/<int:state_id>', views.game_mottos_correct, name='game_mottos_correct'),
    path('game/mottos_incorrect/<int:state_id>', views.game_mottos_incorrect, name='game_mottos_incorrect'),
    path('game/mottos_correct_answer/<int:state_id>', views.game_mottos_correct_answer, name='game_mottos_correct_answer'),
    path('game/mottos_incorrect_answer/<int:state_id>', views.game_mottos_incorrect_answer, name='game_mottos_incorrect_answer'),
]
