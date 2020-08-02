from django.db import models

# Create your models here.
class Jobs(models.Model):
    image  = models.ImageField(upload_to='images/')
    topic = models.CharField(max_length=200,null=True)
    summary = models.TextField(null=True)

    def __str__(self):
        return self.summary

class Certificates(models.Model):
    image  = models.ImageField(upload_to='images/')
    proof = models.URLField(max_length=300,null=True)
    issue = models.CharField(max_length=100,null=True)
    ref = models.CharField(max_length=200,null=True)
    topic = models.CharField(max_length=200,null=True)
    summary = models.TextField(null=True)

    def __str__(self):
        return self.summary

class Publications(models.Model):
    image  = models.ImageField(upload_to='images/')
    topic = models.CharField(max_length=200,null=True)
    summary = models.TextField(null=True)
    proof = models.URLField(max_length=300,null=True)

    def __str__(self):
        return self.summary
