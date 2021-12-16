from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import uploadfile, uploadxmlfile
from pikepdf import Pdf, PdfError, PasswordError
import xml.dom.minidom
import os
import xml.etree.ElementTree as ET


@receiver(post_save, sender=uploadfile)
def fileupload(sender, instance, created, **kwargs):
    
    
    if created and instance.file:
        print('pdf file is uploaded')
        file = instance.file
        try:
            count = Pdf.open(file)
            instance.pagecount = len(count.pages)
        except PasswordError:
            instance.passwordprotected = True
        except Exception as e:
            print(e)
        instance.save()

@receiver(post_save, sender=uploadxmlfile)
def xmlfileupload(sender, instance, created, **kwargs):
    
    if created and instance.xmlfile:
        
        print('xml file is uploaded')
        file = instance.xmlfile
        print(file)
        extension = os.path.splitext(file.name)
        print(extension[1])
        doc=xml.dom.minidom.parse(file)
        rows = doc.getElementsByTagName('row')
        print(rows.length)
        for i in range(rows.length):
            name = doc.getElementsByTagName("name")[i]
            instance.name = instance.name+(name.firstChild.data)+" "
            email = doc.getElementsByTagName("email")[i]
            instance.email = instance.email+(email.firstChild.data)+" "
            password = doc.getElementsByTagName("password")[i]
            instance.password = instance.password+(password.firstChild.data)+" "    
        instance.save()
    

        




