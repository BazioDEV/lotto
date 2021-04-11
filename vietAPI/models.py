from django.db import models

class hanoi_special(models.Model):
    title = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    Four = models.CharField(max_length=50)
    Three = models.CharField(max_length=50)
    Two = models.CharField(max_length=50)
