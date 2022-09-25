from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name

class State(models.Model):
    name = models.CharField(max_length=150)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class District(models.Model):
    name = models.CharField(max_length=150)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name

class City(models.Model):
    name = models.CharField(max_length=150)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name