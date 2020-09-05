from django.contrib.auth.models import User
from django.db import models


# Create your models here.

def profile_image(instance, filename):
    ext = filename.split('.')[-1]
    return 'image/user_{0}.{1}'.format(instance.user.id, ext)

class Member(models.Model):
    GENDER = [
        ('F', 'Female'),
        ('M', 'Male')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DOB = models.DateField()
    about = models.TextField()
    image = models.ImageField(null=True, upload_to=profile_image)
    gender = models.CharField(choices=GENDER, max_length=30)
    address = models.TextField()
    fav_color = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username
