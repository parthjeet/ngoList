from django.db import models

# NGO Table model

class NgoTable(models.Model):
    LOCATION = models.CharField(max_length=200)
    TARGET_GROUPS = models.CharField(max_length=200)
    ORGANIZATION = models.CharField(max_length=200)
    TYPE_OF_BENEFIT = models.CharField(max_length=200)
    WHAT_WILL_BE_PROVIDED = models.CharField(max_length=200)
    DONATION_LINKS_INFO= models.CharField(max_length=200)
    Exemptions = models.CharField(max_length=200)
