from django.db import models

from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    # email = models.EmailField('email address', max_length=255, unique=True)
    pass
