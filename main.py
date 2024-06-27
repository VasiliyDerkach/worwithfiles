from pprint import pprint
file_nam= 'test0.txt'
ftest= open(file_nam, mode='r',encoding='utf8')
contex= ftest.read()
ftest.close()
pprint(contex)