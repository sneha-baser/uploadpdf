from django.db import models

# Create your models here.
class uploadfile(models.Model):
    title = models.CharField(max_length=30 , blank=True)
    desc = models.CharField(max_length=100,blank=True)
    file = models.FileField(blank=True)
    pagecount = models.IntegerField(default=0)
    passwordprotected = models.BooleanField(default=False)
    def __str__(self):
        return self.title