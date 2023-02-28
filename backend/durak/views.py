from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import *
import json
from django.core import serializers

# Create your views here.
def index(request):
    if request.method == "POST":
        pass
    
    else:
        return JsonResponse({
            "durak" : "game"
        })

def save_win(request):
    if request.method == "POST":
        win = BotGame.objects.create(winner=1)

def get_games(request):
    if request.method == "GET":
        # Serializer should be more complex and show less data later on
        games = list(BotGame.objects.all())
        games_json = serializers.serialize("json", games)

        return HttpResponse(games_json, content_type="application/json")