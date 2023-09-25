def somar(n1, n2):
  return n1 + n2

def subtrair(n1, n2):
  return n1 - n2

def multiplicar(n1, n2):
  return n1 * n2

def dividir(n1, n2):
  if n2 == 0:
    return "Não é possível dividir um número por 0"
  else:
    resultado = n1 / n2
    return resultado

def calcular(n1, n2, operador):
  match operador:
    case "+": return somar(n1, n2)
    case "-": return subtrair(n1, n2)
    case "*": return multiplicar(n1, n2)
    case "/": return dividir(n1, n2)
    case other: return "Operador não encontrado"

print(calcular(5, 10, "+"))
print(calcular(5, 10, "-"))
print(calcular(5, 10, "*"))
print(calcular(5, 0, "/"))
print(calcular(5, 10, "o"))


