first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
first_result=[len(g) for g in first_strings if len(g)>=5]
print(first_result)

second_result = [(a, b) for a in first_strings for b in second_strings if len(a)==len(b)]
print(second_result)

third_result={keywrd: len(keywrd) for keywrd in first_strings+second_strings if not len(keywrd)%2 }
print(third_result)