from django.db import models

# Create your models here.
class Articlemodel(models.Model):
    Article_name=models.CharField(max_length=40)
    Article_date = models.DateField()
    Article_writer = models.CharField(max_length=20)
    Article_reviews = models.CharField(max_length=30)


