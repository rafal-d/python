# Zbór zadań B - zadanie 10
# Napisz program fitness obliczający BMI
# wzor = masa / (wzrost) **2
# np: 70 /(1.75)**2
# autor :  Rafał D.
import string

print('Kalkulator BMI \n')
print('Podaj swoją masę ciała: ')
masaCiala = int(input())
print('Podaj swój wzrost: ')

wzrost = int(input())
wzrost = wzrost / 100

bmi = masaCiala / wzrost**2

print('Twoje BMI to {:2.2f}'.format(bmi))