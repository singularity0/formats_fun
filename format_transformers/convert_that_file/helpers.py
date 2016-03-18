import os
import textract
from prettytable import PrettyTable

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_to_files =  base + '/media/temp/'
path_to_result = base + '/format_transformers/'


def convert(uploaded_file):
    ext_format = uploaded_file.split('.')[-1]

    file_dir = path_to_files + uploaded_file

    data = textract.process(file_dir)

    if ext_format == 'xls':
        data = convert_from_xml(data)


    with open(path_to_result+'result.txt', "w") as text_file:
        text_file.write(data)


def convert_from_xml(data):
    for el in data.split('\n'):
            if el != '':
                first_line_headers = el
                break
    t = PrettyTable()
    t.field_names = first_line_headers.split(' ')

    for el in data.split('\n'):
        row = [el for el in el.split(' ') if el != '']
        try:
            if row != first_line_headers.split(' '):
                t.add_row(row)
        except:
            continue
    
    return t.get_string()


