# Zbór zadań A - zadanie 3
# Napisz program liczący silnie rekurencyjnie
# autor :  Rafał D.


def silnia(n):
    if n > 1:
        return n*silnia(n-1)
    else:
        return 1


print('Program zwraca silnie podanej liczby rekurencyjnie \n')
print('Podaj liczbę dla której chcesz obliczyć silnie: ')

liczba = int(input())

wynik = silnia(liczba)
print(wynik)