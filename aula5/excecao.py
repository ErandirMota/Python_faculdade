'''
try:
  n1 = int(input("Número 1: "))
  n2 = int(input("Número 2: "))

  resultado = n1 / n2

  print(f"O resultado da divisão é {resultado}")

except Exception as erro:
  print(f"Ocorreu um erro: {erro}")
'''

try:
  n1 = int(input("Número 1: "))
  n2 = int(input("Número 2: "))

  resultado = n1 / n2

  print(f"O resultado da divisão é: {resultado}")

except ValueError:
  print("Favor digitar somente números")

except ZeroDivisionError:
  print("Não é possivel dividir um número por 0")

except Exception as erro:
  print("Ocorreu um erro ", erro)

else:
  print("O programa foi executado corretamente")