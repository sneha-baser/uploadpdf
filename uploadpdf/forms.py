from django import forms

from .models import uploadfile

class uploadfileForm(forms.ModelForm):

    class Meta:
        model = uploadfile
        fields = '__all__'