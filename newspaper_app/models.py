from django.db import models

import manage

# Create your models here.
class newspaper_db(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    class Meta:
        db_table = 'newspaper_obj'
        managed = False 
        #this is to not manipulate the existing table
