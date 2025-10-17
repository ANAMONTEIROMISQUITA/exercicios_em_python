# 2. Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print(f"A temperatura em Celsius é: {celsius:.2f}°C")