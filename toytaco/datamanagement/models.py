from django.db import models

# Create your models here.
class Asset_Type(models.Model):
    name = models.CharField(max_length=50)

class Asset(models.Model):
    pretty_name = models.CharField(max_length=50)
