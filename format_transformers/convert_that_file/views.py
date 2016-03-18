from django.shortcuts import render
from helpers import convert
from .forms import UploadForm

from .models import UploadedFile

#from .forms import UploadedFileForm


def convert_menu(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            # form.save()

            up_file = UploadedFile(up_file=request.FILES['file_name'])
            up_file.save()

            uploaded_file_name = str(request.FILES['file_name'])

            convert(uploaded_file_name)

        else:
            # return
            print("FORM is NOT VALID**********")

    else:
        form = UploadForm()
    return render(request, 'index.html', locals())




