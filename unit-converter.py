#!/usr/bin/python3

# Simples conversor de unidades. Para rodar, abrir um terminal na pasta que o programa estiver, em um sistema com Python 3 instalado, escrever "python unit-converter.py" e apertar enter.

# tenta converter uma variavel para uma int, e retorna um erro se nao conseguir
def try_convert_int(i):
    try:
        int(i)
        return 1
    except ValueError:
        return 0


print("Bem vindo ao conversor de unidades! Qual unidade voce quer converter para qual?")
print("(1) Centimetro para Polegada")
print("(2) Polegada para Centimetro")
print("(3) Metro para Pes")
print("(4) Pes para Metro")
print("(5) Kilometro para Milha")
print("(6) Milha para Kilometro")
print("(7) Celsius para Fahrenheit")
print("(8) Fahrenheit para Celsius")
print("(9) Kilo para Libra")
print("(0) Libra para Kilo")

choice = input("Por favor escreva o numero desejado: ")

while not try_convert_int(choice) or int(choice) < 0 or int(choice) > 9:
    choice = input("O numero inserido nao corresponde a lista. Por favor escolha de novo: ")

choice = int(choice)


quantity = input("Qual a quantidade? ")
while not try_convert_int(quantity):
    quantity = input("Numero invalido. Por favor insira de novo: ")

if choice == 1:
    value = int(quantity) * 0.39
    print(quantity + " centimetros equivale " + str(value) + " polegadas")
elif choice == 2:
    value = int(quantity) * 2.54
    print(quantity + " polegadas equivale " + str(value) + " centimetros")
elif choice == 3:
    value = int(quantity) * 3.28
    print(quantity + " metros equivale " + str(value) + " pes")
elif choice == 4:
    value = int(quantity) * 0.30
    print(quantity + " pes equivale " + str(value) + " metros")
elif choice == 5:
    value = int(quantity) * 0.62
    print(quantity + " kilometros equivale " + str(value) + " milhas")
elif choice == 6:
    value = int(quantity) * 1.6
    print(quantity + " milhas equivale " + str(value) + " kilometros")
elif choice == 7:
    value = (int(quantity) * 1.8) + 32
    print(quantity + " celsius equivale " + str(value) + " fahrenheit")
elif choice == 8:
    value = (int(quantity) - 32) / 1.8
    print(quantity + " fahrenheit equivale " + str(value) + " celsius")
elif choice == 9:
    value = int(quantity) * 2.2
    print(quantity + " kilos equivale " + str(value) + " libras")
elif choice == 0:
    value = int(quantity) * 0.454
    print(quantity + " libras equivale " + str(value) + " kilos")
