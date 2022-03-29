from django.contrib import admin
from .models import uploadfile,uploadxmlfile , uploadcsvfile, Configuration
# Register your models here.
admin.site.register(uploadfile)
admin.site.register(uploadxmlfile)
admin.site.register(uploadcsvfile)
admin.site.register(Configuration)


