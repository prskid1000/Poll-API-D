from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Voter(models.Model):
    name = models.CharField(max_length=100)
    party_prefered = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    age = models.IntegerField(default=18)

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=100)
    winning_party = models.CharField(max_length=100,default="None")
    winner=models.CharField(max_length=100,default="None")
    opposition_party = models.CharField(max_length=100,default="None")
    opposition=models.CharField(max_length=100,default="None")

    def __str__(self):
        return self.name
