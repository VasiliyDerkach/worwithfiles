import io
#from pprint import pprint
file_nam= 'test0.txt'
with open(file_nam, mode='r',encoding='utf8') as file1:
    for ln in file1:
        print(ln, end='')
