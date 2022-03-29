from .models import uploadfile, uploadxmlfile , uploadcsvfile
from celery import shared_task
from pikepdf import Pdf



@shared_task(bind=True)
def pdf_file_upload(self, id):
    obj = uploadfile.objects.get(id=id)
    obj.isPdfFileUploaded = True
    try:
        file = obj.pdf_file
        count = Pdf.open(file)
        obj.pagecount = len(count.pages)
        
        obj.isPageCountChecked = True

    except Exception as e:
        print(e)
    obj.isPdfSaved = True
    obj.save()
    return "pdf is uploaded and saved"


@shared_task(bind=True)
def xml_file_upload(self, id):
    obj = uploadxmlfile.objects.get(id=id)
    obj.isXmlFileUploaded = True
    obj.xmlNameParseCompleted = True
    obj.xmlEmailParseCompleted = True
    obj.xmlPasswordParseCompleted = True
    obj.save()
    return "xml uploaded"
@shared_task(bind=True)
def csv_file_upload(self, id):
    obj = uploadcsvfile.objects.get(id=id)
    obj.isCsvFileUploaded = True
    obj.save()
    return "csv uploaded"
