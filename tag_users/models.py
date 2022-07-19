from django.db import models

# Create your models here.
class User(models.Model):
    Username = models.CharField(primary_key = True, max_length=50)
    Password = models.CharField(max_length=50)
    Email = models.CharField(default = "",max_length=50)
    EasyGoing = models.IntegerField(default=0)
    Ambitious = models.IntegerField(default=0)
    DogLover = models.IntegerField(default=0)
    StarWarsFan = models.IntegerField(default=0)
    Gamer = models.IntegerField(default=0)
    BasketballFan = models.IntegerField(default=0)
    MorningPerson = models.IntegerField(default=0)
    NightOwl = models.IntegerField(default=0)
    NatureLover = models.IntegerField(default=0)
    Homebody = models.IntegerField(default=0)
    ThrillSeeker = models.IntegerField(default=0)
    FilmBuff = models.IntegerField(default=0)
    BeatlesFan = models.IntegerField(default=0)



    def __str__(self):
        return self.Username



