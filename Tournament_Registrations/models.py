from django.db import models

# Create your models here.
class Cricket_team(models.Model):
    batch = models.IntegerField()
    team_name = models.CharField(max_length=50)
    team_size = models.IntegerField()
    captain_email = models.EmailField()
    captain_name = models.CharField(max_length=128)
    team = models.TextField()

    def __str__(self) -> str:
        return self.captain_name
    
    def __len__(self) -> int:
        return self.team_size

class Football_team(models.Model):
    batch = models.IntegerField()
    team_name = models.CharField(max_length=50)
    team_size = models.IntegerField()
    captain_email = models.EmailField()
    captain_name = models.CharField(max_length=128)
    team = models.TextField()

    def __str__(self) -> str:
        return self.captain_name
    
    def __len__(self) -> int:
        return self.team_size

class Volleyball_team(models.Model):
    batch = models.IntegerField()
    team_name = models.CharField(max_length=50)
    team_size = models.IntegerField()
    captain_email = models.EmailField()
    captain_name = models.CharField(max_length=128)
    team = models.TextField()

    def __str__(self) -> str:
        return self.team_name
    
    def __len__(self) -> int:
        return self.team_size

class Basketball_team(models.Model):
    batch = models.IntegerField()
    team_name = models.CharField(max_length=50)
    team_size = models.IntegerField()
    captain_email = models.EmailField()
    captain_name = models.CharField(max_length=128)
    team = models.TextField()

    def __str__(self) -> str:
        return self.team_name
    
    def __len__(self) -> int:
        return self.team_size
