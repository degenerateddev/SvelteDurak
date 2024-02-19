from django.urls import path
from . import views

urlpatterns = [
    path("save-win/", views.save_win, name="save-win"),
    path("game/", views.get_games, name="games")
]