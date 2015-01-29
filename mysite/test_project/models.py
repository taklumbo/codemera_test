from django.db import models

class Zone(models.Model):
    """ Represents a zone within a country """
    
    code = models.CharField(max_length=1, primary_key=True)
    
    def __str__(self):           
        return self.code

class Province(models.Model):
    """ Represents a province within a country """
    
    code = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    zone = models.ForeignKey(Zone)
    
    def __str__(self):           
        return self.name

class Municipality(models.Model):
    """ Represents a municipality within a province """
    
    code = models.CharField(max_length=50, primary_key=True)
    province = models.ForeignKey(Province)
    name = models.CharField(max_length=200)
    
    def __str__(self):           
        return self.name

    