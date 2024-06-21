from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # The database will store 'M' and 'F'
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    TEAM_CHOICE = (
        ("Doosan", "Doosan Bears"),
        ("KT", "Kia Tigers"),
        ("Kiwoom", "Kiwoom Heroes"),
        ("KT", "KT Wiz"),
        ("LG", "LG Twins"),
        ("NC", "NC Dinos"),
        ("Samsung", "Samsung Lions"),
        ("SSG", "SSG Landers"),
        ("Hanwha", "Hanwha Eagles"),
        ("Lotte", "Lotte Giants"),
        ("None", "None")
    )

    name = models.CharField(max_length=10, unique=True)
    age = models.IntegerField(default = 0)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    team = models.CharField(max_length=8, choices=TEAM_CHOICE)

    def __str__(self):
        return self.name
