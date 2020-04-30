# Zbór zadań A - zadanie 5
# Napisz program sprawdzający, czy podana liczba jest liczbą pierwszą
# autor :  Rafał D.

print('Program sprawdza czy podana liczba jest liczbą pierwszą')
print('Jeśli chesz zakończyć działanie programu wpisz 0 \n')
print ('Podaj liczbę i zobacz czy jest liczbą pierwszą: ')
liczba = int(input())

while True:
   
    if liczba == 0:
        break
    elif liczba == 1 :
        print('Upss ! To nie jest liczba pierwsza')
    elif liczba == 2:
        print ('Udało się ! Znalazłeś liczbę pierwszą',liczba)
    elif liczba == 3:
        print ('Udało się ! Znalazłeś liczbę pierwszą',liczba)
    elif liczba == 5:
        print ('Udało się ! Znalazłeś liczbę pierwszą',liczba)
    elif liczba == 7:
        print ('Udało się ! Znalazłeś liczbę pierwszą',liczba)
    elif liczba % 2 and liczba % 3 and liczba % 5 and liczba % 7 :
        print('Udało się ! Znalazłeś liczbę pierwszą', liczba)
    else:
        print('Upss ! To nie jest liczba pierwsza')
    print ('Podaj liczbę i zobacz czy jest liczbą pierwszą:  ')
    liczba = int(input())