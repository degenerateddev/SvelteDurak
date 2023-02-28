from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("save-win/", views.save_win, name="save-win"),
    path("get-games/", views.get_games, name="get_games")
]