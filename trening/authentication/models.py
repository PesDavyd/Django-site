from django.db import models

class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    birthday = models.DateField(blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.login