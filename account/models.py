from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(
        verbose_name='Contact Number',
        max_length=13,
        blank=True,
        null=True,
        default=''
    )
    user_type = models.CharField(
        choices=(
        ('user','user'),
        ('admin','admin')
        ),
        default='user',
        max_length=10
    )
class UserExtra(models.Model):
    address = models.TextField(
        max_length=1000,
        null=True,
        blank=True
    )
    gender = models.IntegerField(
        choices=(
            (0,'Male'),
            (1,'Female')
        ),
        default=0
    )
    issuer_id=models.ImageField(
        max_length=300,
        upload_to="id proof",
    )
    issuer_image=models.ImageField(
        verbose_name="profile",
        max_length=300,
        upload_to="profile",
    )
    user = models.ForeignKey( 
        to=User,
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.user.username
