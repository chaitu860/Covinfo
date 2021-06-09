from django.db import models
class newspoint(models.Model):
    headline=models.CharField(max_length=200)
    desc=models.URLField(max_length=300,default="covid")
    img=models.URLField()

# Create your models here.
