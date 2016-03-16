from django.shortcuts import render

# Create your views here.


def convert_menu(request):

    return render(request, 'index.html', locals())


def convert_mp3(request):

    return render(request, 'index.html', locals())
