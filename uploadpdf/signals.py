from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import uploadfile, uploadxmlfile, uploadcsvfile , Configuration
from pikepdf import Pdf, PdfError, PasswordError
import xml.dom.minidom
import os
import tabula
import xml.etree.ElementTree as ET
from .tasks import pdf_file_upload
from .tasks import xml_file_upload
from .tasks import csv_file_upload
import csv
from django.core.files import File
from urllib.request import urlretrieve

@receiver(post_save, sender=uploadfile)
def fileupload(sender, instance, created, **kwargs):
    
    
    if created and instance.file:
        compare=Configuration.objects.latest().pagelimit
        file = instance.file
        extension = os.path.splitext(file.name)
        try:
                count = Pdf.open(file)
                instance.pagecount = len(count.pages)
                if(compare<instance.pagecount):
                    instance.PageLimitExceeded=True
                instance.save() 
 
        except PasswordError:
            instance.passwordprotected = True
            print(instance.passwordprotected)
        except Exception as e:
            print(e)
       

        
        
        
        


@receiver(post_save, sender=uploadfile)
def pdf_file_uploaded(sender, instance, created, **kwargs):
    if created:
        pdf_file_upload.delay(instance.id)


@receiver(post_save, sender=uploadxmlfile)
def xmlfileupload(sender, instance, created, **kwargs):
    
    if created and instance.xmlfile:
        
        file = instance.xmlfile
        extension = os.path.splitext(file.name)
        doc=xml.dom.minidom.parse(file)
        rows = doc.getElementsByTagName('row')
        for i in range(rows.length):
            name = doc.getElementsByTagName("name")[i]
            instance.name = instance.name+(name.firstChild.data)+" "
            email = doc.getElementsByTagName("email")[i]
            instance.email = instance.email+(email.firstChild.data)+" "
            password = doc.getElementsByTagName("password")[i]
            instance.password = instance.password+(password.firstChild.data)+" "    
        instance.save()
@receiver(post_save, sender=uploadxmlfile)
def xml_file_uploaded(sender, instance, created, **kwargs):
    if created:
        xml_file_upload.delay(instance.id)


@receiver(post_save, sender=uploadcsvfile)
def csvfileupload(sender, instance, created, **kwargs):
    
    if created and instance.csvfile:
        
        file = instance.csvfile 
        with open(file.path,'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i==0:
                    pass
                else:
                    title=row[0]
                    desc=row[1]
                    url=row[2]
                    uploadfile.objects.create(
                        title=title,
                        desc=desc,
                        file=url
                    )
        instance.save()
@receiver(post_save, sender=uploadcsvfile)
def csv_file_uploaded(sender, instance, created, **kwargs):
    if created:
        csv_file_upload.delay(instance.id)
    

        




