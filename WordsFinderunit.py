import io
punktus = [',', '.', '=', '!', '?', ';', ':', ' - ']
class WordsFinder:
    def __init__(self, *args):
        self.file_names = [a for a in args]

    def get_all_words(self):
        all_words={}
        for file in self.file_names:
            file_lst_words = []
            with open(file,'r','utf-8') as vfile:
                txtfile = vfile.read()
                for line in txtfile:
                    line = line.lower()
                    for char in punktus:
                        line.replace(char, '')
                    lst_words = line.split()
                    file_lst_words+= lst_words
                vfile.close()
            all_words[file]=file_lst_words


if __name__== '__main__':
    tst = WordsFinder('fhggjf','858595690')
    # for u in tst.file_names:
    #     print(u)
    # p = ' fgkgjdfl  fkggjg  rgeptotoert ;rgker;gg'
    # print(p.split())