from django.db import models

# Create your models here.
class Dengue_all(models.Model):
	no = models.IntegerField(primary_key=True)
	date = models.CharField(max_length=10)
	area = models.CharField(max_length=10)
	zone = models.CharField(max_length=10)
	road = models.CharField(max_length=30)
	lon = models.FloatField()
	lat = models.FloatField()