# import itertools
def all_variants(text):
    l = len(text)
    for i in range(1,l+1):
        for j in range(0,l-1):
            if i+j<=l:
                a = text[j:j+i]
                yield text[j:j+i]
            else:
                continue

a = all_variants("abc")
for i in a:
    print(i)
