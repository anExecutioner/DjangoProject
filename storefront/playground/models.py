from django.db import models

# Create your models here.

class Topic(models.Model):

    top_name = models.CharField(max_length=264,unique=True)
    reg = models.CharField(max_length=264, unique = True)

    def __str__(self):
        return self.top_name

class WebPage(models.Model):

    topic  = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length= 264, unique=True)
    url = models.URLField( unique=True)

    def __str__(self):
        return self.name