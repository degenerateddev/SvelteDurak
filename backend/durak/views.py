from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.views import Response

from .models import BotGame
from .serializers import BotGameSerializer

@api_view(["POST"])
def save_win(request):
    serialize = BotGameSerializer(data=request.data)
    if serialize.is_valid(raise_exception=True):
        win = serialize.save()

        serialized = BotGameSerializer(win)

        return Response(serialized.data)

@api_view(["GET"])
def get_games(request):
    games = BotGame.objects.all()
    serialized = BotGameSerializer(games, many=True)

    return Response(serialized.data)