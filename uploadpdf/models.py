from django.db import models



# Create your models here.
class uploadfile(models.Model):
    title = models.CharField(max_length=30 , blank=True)
    desc = models.CharField(max_length=100,blank=True)
    file = models.FileField(blank=True)
    pagecount = models.IntegerField(default=0)
    passwordprotected = models.BooleanField(default=False)
    PageLimitExceeded = models.BooleanField(default=False)
    isPdfFileUploaded = models.BooleanField(default=False)
    isPageCountChecked = models.BooleanField(default=False)
    isPdfSaved = models.BooleanField(default=False)




    def __str__(self):
        return self.title
class uploadxmlfile(models.Model):
    title = models.CharField(max_length=30 , blank=True)
    desc = models.CharField(max_length=100,blank=True)
    xmlfile = models.FileField(blank=True)
    idno = models.IntegerField(default=0)
    name = models.CharField(max_length=30 , blank=True)
    xmlNameParseCompleted = models.BooleanField(default=False)
    email = models.CharField(max_length=30 , blank=True)
    xmlEmailParseCompleted = models.BooleanField(default=False)
    password = models.CharField(max_length=30 , blank=True)
    xmlPasswordParseCompleted = models.BooleanField(default=False)
    isXmlFileUploaded = models.BooleanField(default=False)


    def __str__(self):
        return self.title        
class Configuration(models.Model):
    pagelimit = models.IntegerField(default=5)
    class Meta:
        get_latest_by = ['pagelimit']


      

class uploadcsvfile(models.Model):
    title = models.CharField(max_length=30 , blank=True)
    desc = models.CharField(max_length=100,blank=True)
    csvfile = models.FileField(blank=True)
    isCsvFileUploaded = models.BooleanField(default=False)

    def __str__(self):
        return self.title        

