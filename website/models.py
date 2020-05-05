from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


PRIORITY_CHOICES = (
	(1, 'LOW'), 
	(2, 'MEDIUM'), 
	(3, 'HIGH'), 
	(4, 'EXTREME'),
)
# Create your models here.
class Flare(models.Model):
	"""A flare to inform during a disaster"""
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	date_added = models.DateTimeField(auto_now_add=True)
	priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
	tags = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	latitude = models.FloatField()
	longitude = models.FloatField()
	owner = models.ForeignKey(User, null=True)

	def __str__(self):
		"""Returns the title of a flare for identification"""
		return self.title
