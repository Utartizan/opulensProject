from django.db import models

class UserAccount(models.Model):
    username = models.CharField(max_length=101)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
