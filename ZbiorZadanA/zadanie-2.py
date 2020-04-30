# Zbór zadań A - zadanie 2
# Napisz program zawierający funkcję zwracającą silnię liczby podanej jako argument. Wskazówka : Policz silnię iteracyjnie
# autor :  Rafał D.

def silnia(n):
    silnia = 1
    for i in range(1,n+1):
        silnia *= i
    print('Silnia z liczby: ' + str(n) + ' to: '+ str(silnia))

print('Program zwraca silnie podanej liczby iteracyjnie \n')
print('Podaj liczbę dla której chcesz obliczyć silnie: ')

liczba = int(input())

silnia(liczba)