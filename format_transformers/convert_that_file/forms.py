from django import forms
from .models import History


class UploadForm(forms.Form):
    FORMAT_CHOICES = [
        # <option value='S'>Small</option>
        ('mp3', 'MP3'),
        ('wav', 'WAV'),
        ('xls', 'XLS'),
        ('doc', 'DOC')
    ]

    file_formats = forms.ChoiceField(FORMAT_CHOICES)
    file_name = forms.FileField()

# file_name = FileBrowseField("Browse", max_length=200,extensions=[".jpg", ".doc", ".xls", ".wav"], blank=True, null=True)


class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = '__all__'
