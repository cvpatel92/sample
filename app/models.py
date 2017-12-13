from django.db import models

# Create your models here.



class Info (models.Model):

    Process_ID=models.IntegerField()
    start_time= models.CharField(max_length=30)
    end_time= models.CharField(max_length=30)


