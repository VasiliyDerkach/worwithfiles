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
        for key_file, words_of_file in self.get_all_words():
            i_word= words_of_file.index(word.lower())
            if i_word>=0:
                dct[key_file]=i_word
        return dct



if __name__== '__main__':
    tst = WordsFinder('abra.txt','cadabra.txt')
    dct = tst.get_all_words()
    g= ['gg','oo1t','tyu','oot']
    print(g.index('oot'))
    #print(dct)
    # for u in tst.file_names:
    #     print(u)
    #