from rest_framework import serializers

from .models import BotGame

class BotGameSerializer(serializers.ModelSerializer):
    winner = serializers.CharField(required=True)
    play_date = serializers.DateTimeField(format="%d-%m-%Y#%H:%M:%S")

    class Meta:
        model = BotGame
        fields = ("__all__")
    
    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        return super().create(validated_data)