from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters

class User(AbstractUser):
    nickname = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        validators=[validate_no_special_characters],
        error_messages={'unique': '使えないユーザーネームです。'},
    )
    line_id = models.CharField(
        max_length=20, 
        null=True,
        validators=[validate_no_special_characters],)
    address = models.CharField(
        max_length=40, 
        null=True,
        validators=[validate_no_special_characters],)
    
    def __str__(self):
        return self.email
    