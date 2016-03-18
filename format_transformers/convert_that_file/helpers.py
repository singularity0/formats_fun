import textract
import pickle
import os


def convert(uploaded_file):
    avail_formats = {
        'mp3': convert_from_mp3,
        'doc': convert_from_mp3,
        'xls': convert_from_mp3,
        'wav': convert_from_mp3,
        'jpg': convert_from_mp3,
        'jpeg': convert_from_mp3
    }
    # uploaded_file = str(request.FILES['file_name'])
    extensions = str(uploaded_file).split('.')[-1]
    # save_file(uploaded_file,  extensions)
    print(extensions)

    return avail_formats[extensions](uploaded_file)

def save_file(up_file, ext):
    pass

    # with open(path, 'w+') as f:
    #     pickle.dump(up_file, f)


def convert_from_mp3(the_file):

    print(the_file)
    print(os.getcwd() + '/convert_that_file/' + str(the_file))
    x = textract.process(os.getcwd() + '/convert_that_file/' + str(the_file))

    f = open(os.getcwd() + '/convert_that_file/' + 'result.txt', 'w+')
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
