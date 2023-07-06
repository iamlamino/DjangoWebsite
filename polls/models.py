from django.db import models


class User(models.Model):
    fist_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    organisation = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


