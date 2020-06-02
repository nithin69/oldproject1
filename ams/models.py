from django.db import models
from django.contrib.auth.models import User


class Events(models.Model):
        month = models.CharField(max_length=255)
        image = models.ImageField(upload_to='media', null=True, blank=True)
        date = models.IntegerField()
        title = models.CharField(max_length=255)
        time = models.CharField(max_length=255, null=True, blank=True)
        location = models.CharField(max_length=255, null=True, blank=True)
        description = models.TextField(null=True, blank=True)
        def __unicode__(self):
                return self.title


class News(models.Model):
        title = models.CharField(max_length=255)
        image = models.ImageField(upload_to='media', null=True, blank=True)
        description = models.TextField(null=True, blank=True)
        phone = models.CharField(max_length=255, null=True, blank=True)
        designation = models.CharField(max_length=255, null=True, blank=True)
        application = models.ImageField(upload_to='media', null=True, blank=True)
        def __unicode__(self):
                return self.title


class Members(models.Model):
        name = models.CharField(max_length=255)
        designation = models.CharField(max_length=255, null=True, blank=True)
        membership = models.CharField(max_length=255, null=True, blank=True,  verbose_name = 'Membership No.')
        description = models.TextField(null=True, blank=True)
        phone = models.CharField(max_length=255, null=True, blank=True)
        image = models.ImageField(upload_to='media', null=True, blank=True, verbose_name = 'Person Image')
        application = models.ImageField(upload_to='media', null=True, blank=True)
        def __unicode__(self):
                return self.name
        def sms(self):
                return '<a href="/sms/"> Send SMS </a>'
        sms.allow_tags = True

class Secretery(models.Model):
        name = models.CharField(max_length=255)
        designation = models.CharField(max_length=255, null=True, blank=True)
        membership = models.CharField(max_length=255, null=True, blank=True,  verbose_name = 'Membership No.')
        description = models.TextField(null=True, blank=True)
        phone = models.CharField(max_length=255, null=True, blank=True)
        image = models.ImageField(upload_to='media', null=True, blank=True, verbose_name = 'Person Image')
        application = models.ImageField(upload_to='media', null=True, blank=True)
        def __unicode__(self):
                return self.name
        class Meta:
                verbose_name_plural = 'Body Members'

class Carosuel(models.Model):
        image = models.ImageField(upload_to='media/carosuel', null=True, blank=True)
        title = models.CharField(max_length=255, null=True, blank=True)

class Youtube(models.Model):
        title = models.CharField(max_length=255)
        video = models.CharField(max_length=255, null=True, blank=True)
        def __unicode__(self):
                return self.title


class Activites(models.Model):
        title = models.CharField(max_length=255, null=True, blank=True)
        image = models.ImageField(upload_to='media', null=True, blank=True)
        description = models.TextField(null=True, blank=True)
        def __unicode__(self):
                return self.title


class Scolarship(models.Model):
        title = models.CharField(max_length=255, null=True, blank=True)
        image = models.ImageField(upload_to='media', null=True, blank=True)
        link = models.CharField(max_length=255, null=True, blank=True)
        description = models.TextField(null=True, blank=True)
        phone = models.CharField(max_length=15, null=True, blank=True)
        def __unicode__(self):
                return self.title
        
class Jobs(models.Model):
        title = models.CharField(max_length=255, null=True, blank=True)
        image = models.ImageField(upload_to='media', null=True, blank=True)
        link = models.CharField(max_length=255, null=True, blank=True)
        description = models.TextField(null=True, blank=True)
        phone = models.CharField(max_length=15, null=True, blank=True)
        def __unicode__(self):
                return self.title

class Resource(models.Model):
        title = models.CharField(max_length=255, null=True, blank=True)
        image = models.ImageField(upload_to='media', null=True, blank=True, verbose_name = 'Cover Image')
        filefield = models.FileField(upload_to='media', null=True, blank=True, verbose_name = 'File')
        link = models.CharField(max_length=255, null=True, blank=True)
        description = models.TextField(null=True, blank=True)
        def __unicode__(self):
                return self.title

#class library(models.Model):
#        book = models.CharField(max_length=255, null=True, blank=True)
#        author = models.CharField(max_length=255, null=True, blank=True)
#        status = models.BooleanField(default=True)
#        form_date = models.DateField(null=True, blank=True)
#        to_date = models.DateField(null=True, blank=True)
#        issued = models.CharField(max_length=255, null=True, blank=True)
#        phone = models.CharField(max_length=15, null=True, blank=True)
#        def __unicode__(self):
#                return self.book

class Contact(models.Model):
        name = models.CharField(max_length=255, null=True, blank=True)
        email = models.CharField(max_length=255, null=True, blank=True)
        phone = models.CharField(max_length=255, null=True, blank=True)
        message = models.TextField(null=True, blank=True)
        def __unicode__(self):
                return self.name



class Video(models.Model):
        title = models.CharField(max_length=255, null=True, blank=True)
        video = models.ImageField(upload_to='media', null=True, blank=True, verbose_name = 'Cover Image')
        filefield = models.FileField(upload_to='media', null=True, blank=True, verbose_name = 'File')
        link = models.CharField(max_length=255, null=True, blank=True)
        description = models.TextField(null=True, blank=True)
        def __unicode__(self):
                return self.title

class Image(models.Model):
        title = models.CharField(max_length=255, null=True, blank=True)
        image = models.ImageField(upload_to='media', null=True, blank=True, verbose_name = 'Cover Image')
        filefield = models.FileField(upload_to='media', null=True, blank=True, verbose_name = 'File')
        link = models.CharField(max_length=255, null=True, blank=True)
        description = models.TextField(null=True, blank=True)
        def __unicode__(self):
                return self.title

class Audio(models.Model):
        title = models.CharField(max_length=255, null=True, blank=True)
        audio = models.ImageField(upload_to='media', null=True, blank=True, verbose_name = 'Cover Image')
        filefield = models.FileField(upload_to='media', null=True, blank=True, verbose_name = 'File')
        link = models.CharField(max_length=255, null=True, blank=True)
        description = models.TextField(null=True, blank=True)
        def __unicode__(self):
                return self.title

class library(models.Model):
        book = models.CharField(max_length=255, null=True, blank=True)
        author = models.CharField(max_length=255, null=True, blank=True)
        status = models.BooleanField(default=True)
        cover = models.ImageField(upload_to='media', null=True, blank=True, verbose_name = 'Cover Image')
	form_date = models.DateField(null=True, blank=True)
        to_date = models.DateField(null=True, blank=True)
        issued = models.CharField(max_length=255, null=True, blank=True)
        phone = models.CharField(max_length=15, null=True, blank=True)
        def __unicode__(self):
                return self.book

class Contact(models.Model):
        name = models.CharField(max_length=255, null=True, blank=True)
        email = models.CharField(max_length=255, null=True, blank=True)
        phone = models.CharField(max_length=255, null=True, blank=True)
        message = models.TextField(null=True, blank=True)
        def __unicode__(self):
                return self.name


class Marquee(models.Model):
        content = models.TextField(null=True, blank=True)
        
        def __unicode__(self):
                return self.content

