from django import forms
from .models.basic_models import UploadReport



class ReportForm(forms.ModelForm):
    class Meta:
        model = UploadReport
        fields = ('title', 'uploader', 'pdf', 'cover')
        
class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()