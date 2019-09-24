import os, time
from hashlib import sha256

PATH = './data'
BLOCK_SIZE = 65536 #64kB

def file_list(path):
    list_dir = os.scandir(path)
    file_list =[]
    for o in list_dir:
        if os.DirEntry.is_file(o):
            file_list.append(o.path)
    return file_list

def calc_one_checksum(file):
    m = sha256()
    dic = {}
    with open(file, 'rb') as f:
        while True:
            data = f.read(BLOCK_SIZE)
            if not data:
                break
            m.update(data)
        #print('file: {} sha256: {}'.format(file, m.hexdigest()))
        dic['file'] = file
        dic['hash'] = m.hexdigest()
        f.close()
    return dic
       

if __name__ == "__main__":
    t0 = time.time()
    for f in file_list(PATH):
        print(calc_one_checksum(f))
    elapsed = time.time() - t0
    msg = '{} files processed in {:.2f}s'
    print(msg.format(len(file_list(PATH)), elapsed ))