from django.db import models

# Create your models here.
class uploadfile(models.Model):
    title = models.CharField(max_length=30 , blank=True)
    desc = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to='documents/',blank=True)
    def __str__(self):
        return self.title