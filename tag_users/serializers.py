from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ['Username','Password','Email','EasyGoing','Ambitious','DogLover','StarWarsFan','Gamer',
                "BasketballFan", "MorningPerson", "NightOwl", "NatureLover", "Homebody","ThrillSeeker","FilmBuff", "BeatlesFan"]

    
    


    
