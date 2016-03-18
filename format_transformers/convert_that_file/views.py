from django.shortcuts import render
from helpers import convert, convert_from_doc
from .forms import UploadForm

from .models import UploadedFile

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

            
        else:
            # return
            print("FORM is NOT VALID**********")

    else:
        form = UploadForm()

    if len(uploaded_file_name) > 0:
        print('goooo****')
        convert(uploaded_file_name)

    return render(request, 'index.html', locals())




