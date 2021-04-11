from django.db import models

class gov_thai(models.Model):
    title = models.CharField(max_length=20)
    FirstPrize = models.CharField(max_length=20)
    ThreeFront = models.CharField(max_length=20)
    ThreeUnder = models.CharField(max_length=20)
    TwoUnder = models.CharField(max_length=20)
    date = models.CharField(max_length=30)
        
    def __str__(self):
        return self.title

class lao_vip(models.Model):
    title = models.CharField(max_length=20)
    Five = models.CharField(max_length=20)
    Four = models.CharField(max_length=20)
    Three = models.CharField(max_length=20)
    Two = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    
    def __str__(self):
        return self.date
    
class lao_lotto(models.Model):
    title = models.CharField(max_length=20)
    Four = models.CharField(max_length=20)
    Three = models.CharField(max_length=20)
    Two = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    
    def __str__(self):
        return self.date
    
class lao_star(models.Model):
    title = models.CharField(max_length=20)
    FourTop = models.CharField(max_length=20)
    ThreeTop = models.CharField(max_length=20)
    TwoTop = models.CharField(max_length=20)
    TwoUnder = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    
    def __str__(self):
        return self.date
    

