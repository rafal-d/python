# Zbór zadań A - zadanie 6
# Napisz program sprawdzający, czy podane słowo jest palindromem
# autor :  Rafał D.

print('Program sprawdza czy podane słowo jest palindromem')
print('Przykładem jest słowo KAJAK czytane od tyłu to KAJAK, czyli jest palindromem')
print('Podaj słowo, które może być palindromem:')

slowo = input()

# odwrocenie slowa
odwroconeSlowo = slowo[::-1]

# sprawdzenie czy podane slowo jest palindromem
if slowo == odwroconeSlowo:
    print('Podane slowo ' + slowo.upper() + ' czytane od tylu jest palindromem ' + odwroconeSlowo.upper())
else:
    print('Podane slowo czytane od tyłu nie jest palindromem')
