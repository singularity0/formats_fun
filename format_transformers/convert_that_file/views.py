from django.shortcuts import render
from .forms import UploadForm

# Create your views here.


def convert_menu(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			#print(form.cleaned_data)
			#form.save()


			# определяне на формата
			# създаване на файла според формата
		 
			uploaded_file = request.FILES['file_name']
			
		else:
			# return 
		    print("FORM is NOT VALID**********")


		

	else:
		form = UploadForm()
	return render(request, 'index.html', locals())

def convert_wav():
	# обработва mp3 -> txt
	pass