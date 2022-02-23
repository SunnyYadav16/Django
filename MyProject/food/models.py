from django.db import models


class dest(models.Model):
    name = models.CharField(max_length=120)
    desc = models.TextField()
    text = models.TextField()
