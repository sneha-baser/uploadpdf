from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import uploadfile
from pikepdf import Pdf, PdfError, PasswordError

@receiver(post_save, sender=uploadfile)
def fileupload(sender, instance, created, **kwargs):
 if created and instance.file:

    print('file is uploaded')
    file = instance.file

    try:
        count = Pdf.open(file)
        instance.pagecount = len(count.pages)
    except PasswordError:
        instance.passwordprotected = True
    except Exception as e:
        print(e)
    instance.save()
