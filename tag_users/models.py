from django.db import models
from sklearn.cluster import KMeans
import pickle
# Create your models here.

def getDefaultTags():
    return {
        "EasyGoing": 0,
        "Ambitious": 0,
        "DogPerson": 0,
        "StarWarsFan": 0,
        "Gamer": 0,
        "BasketballFan": 0,
        "MorningPerson": 0,
        "NightOwl": 0,
        "NatureLover": 0,
        "Homebody": 0,
        "DCFan": 0,
        "ThrillSeeker": 0,
        "FilmBuff": 0,
        "BeatlesFan": 0,
        "MarvelFan": 0,
        "ArtLover": 0,
        "CatPerson": 0,
        "Introverted": 0,
        "StrangerThingsFan": 0,
        "Extroverted": 0,
        "ClassicalMusicFan": 0,
        "CoffeeEnthusiast": 0,
        "Foodie": 0,
        "AnimeFan": 0,
        "GymRat": 0
    }

class User(models.Model):
    Username = models.CharField(primary_key = True, max_length=50)
    Password = models.CharField(max_length=50)
    Email = models.CharField(default = "",max_length=50)
    InterestedLat = models.FloatField(default=0.0)
    InterestedLong = models.FloatField(default=0.0)
    MatchCluster = models.IntegerField(default = -1)
    Tags = models.JSONField(default=getDefaultTags)
    MatchedUser = models.CharField(default = str(Username), max_length = 50)
    Matched = models.BooleanField(default=False)  
    SignedIn = models.BooleanField(default=True)

    def __str__(self):
        return self.Username

    def findCluster(self):
        tags = [[
            self.Tags['EasyGoing'],
            self.Tags['Ambitious'],
            self.Tags['DogPerson'],
            self.Tags['StarWarsFan'],
            self.Tags['Gamer'],
            self.Tags['BasketballFan'],
            self.Tags['MorningPerson'],
            self.Tags['NightOwl'],
            self.Tags['NatureLover'],
            self.Tags['Homebody'],
            self.Tags['DCFan'],
            self.Tags['ThrillSeeker'],
            self.Tags['FilmBuff'],
            self.Tags['BeatlesFan'],
            self.Tags['MarvelFan'],
            self.Tags['ArtLover'],
            self.Tags['CatPerson'],
            self.Tags['Introverted'],
            self.Tags['StrangerThingsFan'],
            self.Tags['Extroverted'],
            self.Tags['ClassicalMusicFan'],
            self.Tags['CoffeeEnthusiast'],
            self.Tags['Foodie'],
            self.Tags['AnimeFan'],
            self.Tags['GymRat']
        ]]
        model = KMeans()
        model = pickle.load(open("/workspace/tag_users/KMeans/model.pkl", "rb"))
        cluster = model.predict(tags)
        print(cluster[0])
        self.MatchCluster = cluster[0]




