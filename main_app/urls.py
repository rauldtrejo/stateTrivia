from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup', views.signup, name='signup'),
    path('game/capitals/', views.game_capitals, name='game_capitals')
]
