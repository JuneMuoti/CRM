from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Lead(models.Model):
    SOURCE_CHOICES={
        ("Youtube","Youtube"),
        ("Whatsapp","Whatsapp"),
        ("Facebook","Facebook"),
    }
    first_name=models.CharField(max_length=50)
    last_name=models.CharField( max_length=50)
    age=models.IntegerField(default=0)
    phoned=models.BooleanField(default=False)
    source=models.CharField(choices=SOURCE_CHOICES, max_length=100)
    profile_picture=models.ImageField(null=True, blank=True)
    special_file=models.FileField(null=True,blank=True)
    agent=models.ForeignKey("Agent", on_delete=models.SET_NULL,null=True)
   
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Agent(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    
   

    


