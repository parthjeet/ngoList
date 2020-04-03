from django.db import models

# NGO Table model

class NgoTable(models.Model):
    STATE_UT = models.CharField(max_length=200)
    SPECIFIC_LOCATION = models.CharField(max_length=200)
    TARGET_GROUPS = models.CharField(max_length=200)
    TYPE_OF_BENEFIT = models.CharField(max_length=200)
    ORGANIZATION = models.CharField(max_length=200)
    INITIATIVE = models.CharField(max_length=200)
    WEBSITE = models.CharField(max_length=200)
    DONATION_LINK = models.CharField(max_length=200)
    DONATION_INFO= models.CharField(max_length=200)
    FOREIGN_DONATION = models.CharField(max_length=200)
    INFO = models.CharField(max_length=200)
