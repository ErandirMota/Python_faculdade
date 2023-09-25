i = 1
continuar = True

while continuar:

  numero = int(input("Qual tabuada?"))

  for i in range(1, 11):
    print(f"{numero} x {i} = {numero*i}")

  continuar = input("Deseja continur? (s/n)")
  continuar = True if continuar == "s" else False