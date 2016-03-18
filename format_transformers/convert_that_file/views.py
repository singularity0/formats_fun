from django.shortcuts import render
from helpers import convert
from .forms import UploadForm

from .models import UploadedFile

import shutil
from helpers import base
#from .forms import UploadedFileForm

uploaded_file_name = ""
def convert_menu(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            # form.save()
            global uploaded_file_name
            uploaded_file_name = str(request.FILES['file_name'])
            up_file = UploadedFile(up_file=request.FILES['file_name'])
            up_file.save()

            convert(uploaded_file_name)

            #delete uploaded files after converting
            shutil.rmtree(base + '/media')
            
        else:
            # return
            print("FORM is NOT VALID**********")

    else:
        form = UploadForm()

    return render(request, 'index.html', locals())




