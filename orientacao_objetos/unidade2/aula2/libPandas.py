import pandas as pd

cidades = [
  {'nome': 'Distrito Federal', 'uf': 'DF', 'população': 1500000},
  {'nome': 'São Paulo', 'uf': 'SP', 'população': 32300000},
  {'nome': 'Rio de Janeiro', 'uf': 'RJ', 'população': 4000000},
  {'nome': 'Fortaleza', 'uf': 'CE', 'população': 1000000}
]

dataFrame = pd.DataFrame(cidades)

ordenada = dataFrame.sort_values(by='população', ascending=False)

print(ordenada)
print()
print(ordenada.head(2)['nome'])