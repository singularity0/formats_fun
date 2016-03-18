from django import forms
from .models import History
import os

class UploadedFileForm(forms.Form):
    up_file = forms.FileField(label = "Uplad a file: ")

class UploadForm(forms.Form):
    FORMAT_CHOICES = [
        # <option value='S'>Small</option>
        ('mp3', 'MP3'),
        ('wav', 'WAV'),
        ('xls', 'XLS'),
        ('doc', 'DOC')
    ]
    file_formats = forms.ChoiceField(FORMAT_CHOICES)

    base_d = os.path.dirname(os.path.realpath(__file__))
    name_of_file = 'temp.{}'.format(file_formats)
    path = base_d + name_of_file

    file_name = forms.FileField()
    # print(str(file_name))
    # print(dir(file_formats))
# file_name = FileBrowseField("Browse", max_length=200,extensions=[".jpg", ".doc", ".xls", ".wav"], blank=True, null=True)


class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = '__all__'
