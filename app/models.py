from django.db import models

# Create your models here.

class Spell(models.Model):
    name = models.CharField(max_length=200) #Campo de txto com limitação 
    description = models.TextField() #Campo de texto sem limitação
     
    def __str__(self):
        return self.name
    
class House(models.Model):
    name = models.CharField(max_length=200)
    description =  models.TextField()

    def __str__(self):
        return self.name
    
class Characters(models.Model):
    image = models.TextField()
    name = models.CharField(max_length=200)
    wizard = models.BooleanField(max_length=200)
    house = models.ForeignKey(House, verbose_name="Character's House", on_delete=models.CASCADE)
    species = models.CharField(max_length=200)
    ancestry = models.CharField(max_length=200)
    eyeColor = models.CharField(max_length=200)
    hairColor = models.CharField(max_length=200)
    actor = models.CharField(max_length=200)
    created = models.DateField(editable=False, auto_now=True)
    
    def __str__(self):
        return self.name
    