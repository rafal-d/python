# Zbór zadań A - zadanie 1
# Napisz program suma.py, który wyświetla sumę dwóch liczb podanych przez użytkownika
# autor :  Rafał D.

print('Program wyświetla sumę dwóch liczb podanych przez użytkownika')
print('Podaj liczbę A: ')

liczbaA = int(input())

print('Podaj liczbę B: ')

liczbaB = int(input())

# definiowanie funkcji
def suma(a, b):
   print('Liczba A to: ' + str(a)+ '\n' + 'Liczba B to: ' + str(b) + '\n' + 'Suma A + B to: ', a+b )

# przekazanie parametrow do funkcji i wyświetlenie wyniku
suma(liczbaA,liczbaB)

