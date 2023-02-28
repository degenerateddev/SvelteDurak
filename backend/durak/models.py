from django.db import models
import uuid
from datetime import datetime

WINNER = (
    ("BOT", "Bot"),
    ("PLAYER", "Player")
)

# Create your models here.
class BotGame(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    winner = models.CharField(choices=WINNER, max_length=20)
    play_date = models.DateTimeField(auto_now_add=True)
