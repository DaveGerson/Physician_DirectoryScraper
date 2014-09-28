__author__ = 'gerson64'

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print(file_len('E:/medicare/Medicare-Physician-and-Other-Supplier-PUF-CY2012.txt'))