numeros = [10, 20, 30, 17, 58, 3, 7]
print(numeros[2])

carros = ["Pálio", "Gol", "Virtus", "Ka", "Onix"]
print("1 ->", carros)

# Adicionando mais um carro no array
carros.append("Kombi")
print("2 ->", carros)

# Removendo carro no array de carros através do nome
carros.remove("Gol")
print("3 ->", carros) 

# Removendo carro no array através da posição
del carros[3]
print("4 ->", carros)

# Ordenando o array de carros em ordem alfabética
carros = sorted(carros)
print("5 ->", carros)

# Exibindo cada carro separadamente
for carro in carros:
  print(carro)