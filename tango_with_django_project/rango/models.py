from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
	class Meta:
		verbose_name_plural = 'Categories'
	def __str__(self): # For Python 2, use __unicode__ too
		return self.name
		
class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)
	
	def __str__(self): # For Python 2, use __unicode__ too
		return self.title
		
class trialModel(models.Model):
	# Below is just a trial model I made to practice creating models
	# the body of the model is actually the Question class from L3-DjangoTutorialLecture1 pg 11
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self): # For Python 2, use __unicode__ too
		return self.question_text