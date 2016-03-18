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
       ('doc', 'DOC'),
       ('pdf', 'PDF'),
       ('csv', 'CSV'),
       ('eml', 'EML'),
       ('epub', 'EPUB'),
       ('json', 'JSON'),
       ('pdf', 'PDF')

   ]
    file_formats = forms.ChoiceField(FORMAT_CHOICES)

    base_d = os.path.dirname(os.path.realpath(__file__))
    name_of_file = 'temp.{}'.format(file_formats)
    path = base_d + name_of_file

    file_name = forms.FileField()

    

class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = '__all__'
