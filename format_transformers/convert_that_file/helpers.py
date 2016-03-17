import textract
import pickle
import os


def convert(uploaded_file):
    avail_formats = {
        'mp3': convert_from_mp3,
        'doc': convert_from_doc,
        'xls': convert_from_xls,
        'wav': convert_from_wav,
        'jpg': convert_from_jpg,
        'jpeg': convert_from_jpg
    }
    # uploaded_file = str(request.FILES['file_name'])
    extensions = str(uploaded_file).split('.')[-1]
    # save_file(uploaded_file,  extensions)


    return avail_formats[extensions](uploaded_file)

def save_file(up_file, ext):
    pass

    # with open(path, 'w+') as f:
    #     pickle.dump(up_file, f)


def convert_from_mp3(the_file):
    x = textract.process('P!nk - So What.mp3')

    f = open('file1.txt', 'r+')
    f.write(x)
    f.close()






    print (42)


def convert_from_doc(the_file):
    pass


def convert_from_xls(the_file):
    pass


def convert_from_wav(the_file):
    pass


def convert_from_jpg(the_file):
    pass
