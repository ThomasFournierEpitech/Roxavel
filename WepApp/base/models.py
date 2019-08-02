from django.db import models
from django.contrib.auth.models import User

class LOLAccountRegistered(models.Model):
    account_id = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (self.name)
