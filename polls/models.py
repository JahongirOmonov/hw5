from django.db import models

# Create your models here.

class PupilModel(models.Model):
    name = models.CharField(default='', max_length=200)
    about_subject = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
    

