from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
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

class Post(models.Model):
    title = models.CharField(max_length=60)
    item_price = models.IntegerField(validators=[MinValueValidator(1)])
    CONDITION_CHOICES = [
        ('새제품', '新品'),
        ('최상', '美品'),
        ('상', '上'),
        ('중', '中'),
        ('하', '下'),
    ]
    item_condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    item_details = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='item_pics')
    image2 = models.ImageField(upload_to='item_pics', blank = True)
    image3 = models.ImageField(upload_to='item_pics', blank = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title