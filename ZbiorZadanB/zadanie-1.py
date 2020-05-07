# Zbór zadań B - zadanie 1
# Napisz program przyjmujący serię oddzielonych przecinkami liczb z konsoli, a zwróci listę oraz krotkę z tych liczb
# przykładowe dane wejściowe : 34,60,55,33,12,98
# autor :  Rafał D.

print('Program pobiera dane wejściowe w formie ciągu liczb odzielonych przecinkiem i wyświetla listę oraz krotkę')
print ('Podaj liczby ( np. 34,60,55,33,12,98 ) : ')
liczby = input()
# użycie metody split(), która usunie przecinki danych wejściowych
liczby2 = liczby.split(',')
# konwertowanie ciągu do postaci listy
newList = list(liczby2)
# konwertowanie ciągu do postaci krotki
newTuple = tuple(liczby2)

print('Podany ciąg liczbowy w postaci listy')
print(newList)
print('Podany ciąg liczbowy w postaci krotki')
print(newTuple)