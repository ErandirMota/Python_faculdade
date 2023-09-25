arquivo = open("pessoas.txt", "w")

arquivo.write("Joao\n")
arquivo.write("Erandir\n")
arquivo.write("Rebeca\n")

arquivo.close()

with open("pessoas.txt", "r+") as arquivoLeitura:
  for linha in arquivoLeitura:
    print(linha)