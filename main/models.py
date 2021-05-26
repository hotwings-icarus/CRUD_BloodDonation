from django.db import models

# Create your models here.

class Donors(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    address = models.TextField(max_length=1000)
    blood_grp= models.CharField(max_length=3)
    rh=models.CharField(max_length=3)
    image = models.ImageField(upload_to="images/")
    consent = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title