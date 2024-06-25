from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, name, age, gender, team, password=None):
        user = self.model(
            username = username,
            name = name,
            age = age,
            gender = gender,
            team = team,
            is_superuser = 0,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, name, age, gender, team, password):
        user = self.create_user(
                username = username,
                name = name,
                age = age,
                gender = gender,
                team = team,
                password = password
            )
        
        user.is_admin = 1
        user.is_superuser = 1
        user.is_staff = 1
        user.save(using=self._db)
        return user


class User(AbstractUser):

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

    name = models.CharField(max_length=10, unique=True, null=False, blank=False)
    age = models.IntegerField(default = 0)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    team = models.CharField(max_length=8, choices=TEAM_CHOICE)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'age', 'gender', 'team']

    def __str__(self):
        return self.name
