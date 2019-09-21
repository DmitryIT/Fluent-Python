import os
from hashlib import sha256

PATH = './data'

def file_list(path):
    list_dir = os.listdir(path)
    file_list =[]
    for o in list_dir:
        print(o)
        if os.path.isfile(o):
            file_list.append(o)
    return file_list

def calc_one_checksum(file):
    with file.open() as f:
        m = sha256()
        m.update(f)
        msg = 'file: {}, sha256: {}'
        print(msg.format(f, m.digest() ))       

if __name__ == "__main__":
    for f in file_list(PATH):
        print(f)