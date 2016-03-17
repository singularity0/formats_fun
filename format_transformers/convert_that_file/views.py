from django.shortcuts import render
from .forms import UploadForm
from .helpers import convert, save_file
# Create your views here.


def convert_menu(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            # form.save()


            # the file object
            uploaded_file = request.FILES['file_name']


            # convert(uploaded_file)

        else:
            # return
            print("FORM is NOT VALID**********")

    else:
        form = UploadForm()
    return render(request, 'index.html', locals())


def convert_wav():

    pass




