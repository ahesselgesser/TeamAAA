from django import forms

from .models import Report



class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('title', 'uploader', 'pdf', 'cover')
        
class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))