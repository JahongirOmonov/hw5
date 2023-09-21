from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.




class StaffUser(AbstractUser):
    CHOICE_ROLES = (
        (3,'admin'),
        (2, 'controller'),
        (1, 'member')
    )

    roles = models.PositiveIntegerField(choices=CHOICE_ROLES, default=1)
