
def convert(uploaded_file):
    avail_formats = {
        'mp3': convert_from_mp3,
        'doc': convert_from_mp3,
        'xls': convert_from_mp3,
        'wav': convert_from_mp3,
        'jpg': convert_from_mp3,
        'jpeg': convert_from_mp3
    }

    format_to_convert = str(uploaded_file).split('.')[-1]
    #print(format_to_convert)

    avail_formats[format_to_convert](uploaded_file)


def convert_from_mp3(the_file):
    pass


def convert_from_doc(the_file):
    pass


def convert_from_xls(the_file):
    pass


def convert_from_wav(the_file):
    pass


def convert_from_jpg(the_file):
    pass
