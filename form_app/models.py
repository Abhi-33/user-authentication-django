from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model) :
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    photo = models.ImageField(upload_to='photos/' , blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True) #It'll automatically update


    def __str__(self):
        return f"{self.user.username}-{self.email[:8]}"
