# Zbór zadań B - zadanie 9
# Napisz program konwertujący wysokość podaną w stopach i calach na centymetry
# autor :  Rafał D.

# 1 cal to 2.54 cm
cal = 2.54
# 1 stopa to 30.48 cm
stopa = 30.48


print('Program konwertuje wysokość podaną w stopach i calach na centymetry')

while True:
    print('Wybierz opcję co chcesz zrobić : \n 1 - stopy na cale,\n 2 - cale na centymetry \n 0 - koniec progrmu')
    print('Jaką opcję wybrałeś: ')
    opcja = input()
    if opcja == '1':
        print('Podaj wysokosc stop do przeliczenia na centymetry :')
        ileStop = int(input())
        stopaCentymetr = ileStop * stopa
        print('Wysokość stop po przeliczeniu na centymetry to: ', stopaCentymetr)
    elif opcja == '2':
        print('Podaj wysokosc stop do przeliczenia na centymetry :')
        ileCali = int(input())
        calCentymetr = ileCali * cal
        print('Wysokość stop po przeliczeniu na centymetry to: ', calCentymetr)
    elif opcja == '0':
        break