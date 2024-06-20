from django.db import models

# Create your models here.
class App (models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255) 
    points = models.IntegerField()


    def __str__(self):
        return self.name
    
    
