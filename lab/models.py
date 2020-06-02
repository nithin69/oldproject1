from django.db import models

# Create your models here.

class Contact(models.Model):

	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	subject = models.CharField(max_length=200)
	message = models.CharField(max_length=200)
	
	def __unicode__(self):
        	return self.name

class Gallery(models.Model):
      
       photo = models.ImageField(null=True, blank=True)
       title = models.CharField(max_length=200, null=True, blank=True)
       description = models.CharField(max_length=200, null=True, blank=True)
	
       def __unicode__(self):
		return self.description
       
