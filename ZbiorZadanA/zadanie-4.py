# Zbór zadań A - zadanie 4
# Napisz program rysujący choinkę o zadanej wielkości
# autor :  Rafał D.

print ('Podaj liczbe calkowita: ')
liczba = int(input())

star = '*'

for i in range(liczba):
    nowa = star * i
    if i % 2:
        print(nowa.center(liczba -1))