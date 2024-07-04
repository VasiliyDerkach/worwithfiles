import io
punktus = [',', '.', '=', '!', '?', ';', ':', ' - ']
class WordsFinder:
    def __init__(self, *args):
        self.file_names = [a for a in args]

    def get_all_words(self):
        all_words={}
        for file in self.file_names:
            file_lst_words = []
            with open(file, mode='r',encoding='utf-8') as vfile:

                for line in vfile:
                    line = line.lower()
                    #print(line,end='')
                    for char in punktus:
                        line = line.replace(char, '')
                    #print(line, end='')
                    lst_words = line.split()
                    #print(lst_words)
                    file_lst_words+= lst_words
                vfile.close()
            all_words[file]=file_lst_words
        return all_words
    def find(self, word):
        dct = {}
        alld = self.get_all_words()
        for key_file, words_of_file in alld.items():
            i_word = 0
            if word.lower() in words_of_file:
                i_word= words_of_file.index(word.lower())
            if i_word>=0:
                dct[key_file]=i_word
        return dct
    def count(self, word):
        dct = {}
        for key_file, words_of_file in self.get_all_words().items():
            dct[key_file]=words_of_file.count(word.lower())
        return dct



if __name__== '__main__':
    tst = WordsFinder('abra.txt','cadabra.txt')
    dct = tst.get_all_words()
    print(dct,dct['cadabra.txt'].count('пусть'))
    dct = tst.find('Чаполино')
    print(dct)
    dct = tst.count('пусть')
    print(dct)
