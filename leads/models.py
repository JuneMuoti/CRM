from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
# pre_save called before something is committed to the DB
# post_save sa called after data is commited to the DB
# listens to when a user is commited to the db
# signals are events that are fired when certain actions take place

# Create your models here.
class User(AbstractUser):
    pass
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

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
    organization=models.ForeignKey("UserProfile",on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username



def post_user_created_signal(sender,instance,created,**kwargs):
    # sender-
    # instance-actual model that was saved
    # created argument tells us where or not this was the moment the model instance was created
    # kwargs captures the rest of the arguments if there are any
    if created:
        UserProfile.objects.create(user=instance)
    print(instance,created)

post_save.connect(post_user_created_signal,sender=User)
# connect takes in the function we want to call and the sender(the model that is sending the event)

   

    


