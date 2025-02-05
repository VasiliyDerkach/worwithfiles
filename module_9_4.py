import random
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name,mode='w', encoding='utf-8')
        for a in data_set:
            file.write(str(a)+'\n')
        file.close()
    return write_everything
class MysticBall:
    def __init__(self,*words):
        self.words = words
    def __call__(self):
        return random.choice(self.words)

if __name__=='__main__':
    first = 'Мама мыла раму'
    second = 'Рамена мало было'
    print(list(map(lambda char, char1: True if char==char1 else False, first, second)))
    write = get_advanced_writer('example.txt')
    write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print(first_ball())
    print(first_ball())
    print(first_ball())
    #print(random.choice(['self','words']))