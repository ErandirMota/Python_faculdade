import csv

carros = [
  {"Vw", "Virtus", "2017"},
  {"Vw", "Gol", "1999"},
  {"Fiat", "Palio", "2002"},
]

with open("carros.csv", "w", newline="") as arquivo:
  fileCSV = csv.writer(arquivo, delimiter=";")

  fileCSV.writerow(["Marca", "Modelo", "Ano"])
  fileCSV.writerows(carros)
