__author__ = 'gerson64'
import sys
import ntpath

splitLen = 704098          # 704098 lines per file
fileName='E:/medicare/'
outputBase = 'medicare_records' # output.1.txt, output.2.txt, etc.
print(ntpath.exists('E:/medicare/'))



input = open('E:/medicare/Medicare-Physician-and-Other-Supplier-PUF-CY2012.txt', 'r')

count = 0
at = 0
dest = None
for line in input:
    if count % splitLen == 0:
        if dest: dest.close()
        dest = open('E:/medicare/splitfile/'+outputBase + str(at) + '.txt', 'w')
        at += 1
    dest.write(line)
    count += 1


