from django.db import models

# Create your models here.
class Asset_Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Asset(models.Model):
    pretty_name = models.CharField(max_length=50)

    def __str__(self):
        return self.pretty_name
