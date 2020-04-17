from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.cache import cache
from quiz import settings
import datetime

class Userprofile(models.Model) :
    def last_seen(self):
        x = cache.get('seen_%s' % self.user.username )
        if x is not None :
            return x
        else :
            return False
    def online(self) :
        now = datetime.datetime.now()
        if self.last_seen() :
            if now > self.last_seen() + datetime.timedelta(seconds=settings.USER_ONLINE_TIMEOUT) :
                return False
            else :
                return True
        else :
             
            return False

            
    user = models.OneToOneField(User,on_delete=models.CASCADE)                                      
        # dob = models.DateField()
    city = models.CharField(max_length=30,default="abc")

def create_profile(sender , **kwargs) :
    if kwargs['created'] :
        new_profile = Userprofile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile , sender=User)
    


 
