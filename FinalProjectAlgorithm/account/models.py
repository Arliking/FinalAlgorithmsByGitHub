from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    age = models.PositiveSmallIntegerField('Age', default=1)
    gender = models.CharField('Gender', choices=GENDER_CHOICE, max_length=255)
    phone_number = models.CharField('Phone number', max_length=255)

    def __str__(self):
        return str({self.username})

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'user'


class ProfileSettings(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_avatar = models.ImageField('Profile image', blank=True, null=True, upload_to='profile_images/')
    entry_draft = models.TextField(blank=True, null=True)

    def __str__(self):
        return str({self.user.username})

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        db_table = 'user_profile'
