from django.db import models
from django.utils import timezone

# Create your models here.

class Building(models.Model):
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 255)
	#lat = models.FloatField()
	#longit= models.FloatField()

	#def __str__(self):
	#	return self.id + ':' + self.name

class User(models.Model):
	ist_id = models.CharField(max_length = 10, primary_key = True)
	name = models.CharField(max_length = 255)
	build_id = models.ForeignKey(Building, on_delete = models.CASCADE)
	range_user = models.IntegerField()
	lat = models.FloatField()
	longit = models.FloatField()

	#def __str__(self):
	#	return self.ist_id


class Messages(models.Model):
	message = models.CharField(max_length = 255)
	build_id = models.ForeignKey(Building, on_delete = models.CASCADE)
	date = models.DateTimeField(auto_now_add = True)