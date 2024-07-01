
def custom_write(file_name, strings):
    newfile= open(file_name,mode='w',encoding='utf8')

    i=0
    strings_positions={}
    for a in strings:
        i+= 1
        b=  newfile.tell()
        strings_positions[(i, b)] = a
        newfile.write(a+'\n')

    newfile.close()
    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test7.txt', info)
for keyrz,elem in result.items():
  print(keyrz,elem)
print('stop')