from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup', views.signup, name='signup'),
    path('game/capitals/<int:state_id>/', views.game_capitals, name='game_capitals'),
    path('game/capitals_incorrect/<int:state_id>', views.game_capitals_incorrect, name='game_capitals_incorrect')
]
