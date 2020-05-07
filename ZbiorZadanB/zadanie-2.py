# Zbór zadań B - zadanie 2
# Napisz program wyświetlający liczby podzielne przez 7 i nie będące wielokrotnością 5 z przedziału 
# 2000 do 3000. Liczby te powinny być wyświetlone w jednej linii i oddzielone przecinkami
# autor :  Rafał D.

import random

print('Program wyświetla liczby podzielne przez 7 i nie będące wielokrotnością 5 z przedziału')
print('2000 do 3000. Liczby te powinny być wyświetlone w jednej linii i oddzielone przecinkami \n')

wynik = ''
for i in range(2000,3000):
    if i % 7 == 0:
        if i % 5 == 0:
            wynik += str(i) + ','

print(wynik)
