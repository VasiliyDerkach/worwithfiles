def personal_sum(numbers):
    incorrect_data = 0
    sum = 0
    for a in numbers:
        try:
            # if str(int(a))==a:
            #     a1 = int(a)
            # else:
            #     a1 = a
            sum+= a
        except TypeError:
            # try:
            #     if str(float(a)) == a:
            #         a1 = float(a)
            #         sum += a1
            # except:
            incorrect_data+= 1
            print(f'Некорректный тип данных для подсчёта суммы -{a}')
        # except ValueError:
        #     try:
        #         if str(float(a)) == a:
        #             a1 = float(a)
        #             sum += a1
        #     except:
        #         incorrect_data+= 1

    return (sum, incorrect_data)
def calculate_average(numbers):
    try:
        sums = personal_sum(numbers)
        sum = sums[0]
        return sum/(len(numbers)-sums[1])
    except ZeroDivisionError:
        return 0
    except TypeError as exx:
        print(f'В numbers записан некорректный тип данных {exx}')
        return None


if __name__ == '__main__':
    # print(personal_sum([50,100,'150',7.8,'Iye','10.8']))
    # print(str(float('10.8'))=='10.8')
    print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

