# Zbór zadań B - zadanie 3
# Napisz program przyjmujący promień koła i obliczający jego pole
# autor :  Rafał D.

print('Proszę podać promień koła:')
promien = int(input())
# stala pi w przyblizeniu
pi = 3.1415
# wzór na obliczenie pola koła 
pole = pi * promien**2

print('Pole koła wynosi: '+ str(pole))